import queue
import socket
import select
import time
from threading import Thread, Event
from queue import Queue

class TcpClient(Thread):
    def __init__(self, host, port):
        super(TcpClient, self).__init__()
        self.host = host
        self.port = port

        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_socket.connect((self.host, self.port))

        self.write_socket, self.tx_ready_socket = socket.socketpair()
        self.tx_queue = queue.Queue()

        self.kill = Event()

    def send(self, data: bytes):
        self.tx_queue.put(data)
        self.write_socket.send(b'\x00')

    def disconnect(self):
        self.kill.set()

    def run(self):
        # RX task
        while not self.kill.isSet():
            rsocks, _, _ = select.select([self.main_socket, self.tx_ready_socket], [], [], 1)
            for s in rsocks:
                if s is self.main_socket:
                    print(s.recv(1024))
                elif s is self.tx_ready_socket:
                    s.recv(1)
                    self.main_socket.sendall(self.tx_queue.get())


if __name__ == '__main__':
    tc = TcpClient('127.0.0.1', 10021)
    tc.start()
    tc.send(b'HELLO')
    tc.send(b'WORLD')
    time.sleep(1)
    tc.send(b'SLOWER')
    time.sleep(1)
    tc.send(b'NOW')
    time.sleep(1)
    tc.disconnect()
    tc.join()
    print('DONE')