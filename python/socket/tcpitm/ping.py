import socket
import sys
from time import sleep
# Create a TCP/IP socket
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

# Set up connection variables
address = '127.0.0.1'
port    = 2000
server_address = ( address, port )
print( 'Connecting to {address}:{port}' )

while True:
    # Connect to server
    sock.connect( server_address )
    try:
        print( 'Connected' )
        # Read data from client and echo back
        while True:
            sock.send( b'ping' )
            data = sock.recv( 1024 )
            if data == b'pong':
                print( 'Got pong!' )
            else:
                print( f'Unknown response: {data}' )
            sleep( 1 )
    finally:
        socket.close()