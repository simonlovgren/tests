import socket
import threading, signal
import argparse
from time import sleep,time

# GLOBALS
killEvent  = threading.Event()
printLock  = threading.Lock()
stopServer = False
stopClient = False
startTime  = time()

# Classes
class Server( object ):
    def __init__( self, host, port ):
        super().__init__()

        # Class members
        self.host     = host
        self.port     = port
        self.clients  = []
        self.clientId = 0

        # Set up socket
        self.sock   = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        self.sock.settimeout( 5 )
        self.sock.bind( ( self.host, self.port ) )

    def run( self ):
        tsPrint( f'Server starting.' )
        self.sock.listen( 5 )
        tsPrint( f'Listening on {self.host}:{self.port}' )
        try:
            while ( not killEvent.is_set() ):
                try:
                    sock, address = self.sock.accept()
                    tsPrint( "Client connected" )
                except socket.timeout:
                    # Timeout for sock.accept, just jump back
                    # to start of while loop
                    continue
                tsPrint( "Creating client thread" )
                # If we get to here, we have a client conneciton
                newThread = ClientThread( self.clientId, address, sock )
                self.clients.append( newThread )
                newThread.start()
                self.clientId += 1
        finally:
            self.sock.close()
        # Here we've been told to die. Wait for client threads to die
        for c in self.clients:
            c.join()

class ClientThread( threading.Thread ):
    def __init__( self, id, address, sock ):
        super().__init__()
        self.id = id
        self.address = address
        self.sock    = sock
        self.bufSize = 1024
        self.socketCloseTimeout = 60
        self.sinceLastMsg       = 0

        self.sock.settimeout( 1 )

        tsPrint( f'New client [{self.id}] connected from {address}' )

    def run( self ):
        try:
            while ( not killEvent.is_set() ):
                try:
                    data = self.sock.recv( self.bufSize )
                    if ( data ):
                        self.sinceLastMsg = 0
                        self.handleMessage( data )
                    else:
                        tsPrint( "Client disconnected." )
                        break
                except socket.timeout:
                    # Socket timed out, check if time to close socket,
                    # otherwise just jump to start of loop
                    if ( self.sinceLastMsg >= self.socketCloseTimeout ):
                        tsPrint( 'Client timed out, closing socket.' )
                        break
                    else:
                        self.sinceLastMsg += 1
                        continue
        finally:
            self.sock.close()
        tsPrint( 'Client thread exiting.' )

    def handleMessage( self, msg ):
        tsPrint( f'[{self.id}] > {msg}' )
        self.sock.sendall( msg )

def killHandler( signum, stackFrame ):
    print('')
    tsPrint( f'Shutting down server.' )
    # Signal kill event
    killEvent.set()

# Functions
def tsPrint( msg ):
    '''
    Thread safe print.
    '''
    printLock.acquire()
    print( f'[{time() - startTime:5.2f}] {msg}' )
    printLock.release()

def main( args ):
    # Retister SIGTERM and SIGINT handler
    signal.signal( signal.SIGINT, killHandler )
    signal.signal( signal.SIGTERM, killHandler )

    s = Server( args.host, args.port )
    s.run()
    tsPrint( f'Server shut down.' )

    return 0

def parseArgs():
    parser = argparse.ArgumentParser( description = 'Multithreaded TCP server.' )

    # host
    parser.add_argument(
        '--host'
        ,action = 'store'
        ,help = 'Host to listen to.'
        ,type = str
        ,default = '127.0.0.1'
    )

    # Port
    parser.add_argument(
        '-p', '--port'
        ,action = 'store'
        ,help = 'Port to listen on.'
        ,type = int
        ,default = 10021
    )

    return parser.parse_args()

# Entry poing
if __name__ == "__main__":
    res = main( parseArgs() )
    if ( res != 0 ):
        print( f'main() returned with error: {res}' )