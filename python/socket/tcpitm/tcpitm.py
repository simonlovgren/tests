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
    def __init__( self, host, port, server, serverport ):
        super().__init__()
        
        # Class members
        self.host       = host
        self.port       = port
        self.server     = server
        self.serverport = serverport
        self.clients    = []
        self.clientId   = 0

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
                newThread = ClientThread( self.clientId, address, sock, self.server, self.serverport )
                self.clients.append( newThread )
                newThread.start()
                self.clientId += 1
        finally:
            self.sock.close()
        # Here we've been told to die. Wait for client threads to die
        for c in self.clients:
            c.join()

class ClientThread( threading.Thread ):
    def __init__( self, id, address, sock, server, serverport ):
        super().__init__()
        self.id = id
        self.address = address
        self.sock    = sock
        self.bufSize = 1024
        self.socketCloseTimeout = 600 # 10min
        self.sinceLastMsg       = 0
        self.server     = server
        self.serverport = serverport

        self.sock.settimeout( 0.1 )

        tsPrint( f'New client [{self.id}] connected from {address}' )

    def run( self ):

        try:
            # Connect to server
            server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            server.settimeout( 0.1 )
            try:
                server.connect( (self.server, self.serverport ) )
            except Exception:
                print( f'Unable to connect to server, closing client [{self.id}]' )
                return

            while ( not killEvent.is_set() ):
                # Client to server communications
                try:
                    data = self.sock.recv( self.bufSize )
                    if ( data ):
                        self.sinceLastMsg = 0
                        tsPrint( f'[{self.id}] [{self.address[0]}:{self.address[1]} --> {self.server}:{self.serverport}]  {data}' )
                        server.sendall( data )
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
                # Server to client communication
                try:
                    data = server.recv( self.bufSize )
                    if ( data ):
                        self.sinceLastMsg = 0
                        tsPrint( f'[{self.id}] [{self.address[0]}:{self.address[1]} <-- {self.server}:{self.serverport}]  {data}' )
                        self.sock.sendall( data )
                    else:
                        tsPrint( "Server disconnected." )
                        break
                except socket.timeout:
                    # Socket timed out, check if time to close socket,
                    # otherwise just jump to start of loop
                    if ( self.sinceLastMsg >= self.socketCloseTimeout ):
                        tsPrint( 'Server timed out, closing socket.' )
                        break
                    else:
                        self.sinceLastMsg += 1
                        continue
        finally:
            self.sock.close()
            server.close()
        tsPrint( 'Client thread exiting.' )

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

    tsPrint( f'Client connects to: {args.client}:{args.clientport}' )
    tsPrint( f'Connecting to:      {args.server}:{args.serverport}' )

    s = Server( args.client, args.clientport, args.server, args.serverport )
    s.run()
    tsPrint( f'Server shut down.' )

    return 0

def parseArgs():
    parser = argparse.ArgumentParser( description = 'Multithreaded TCP server.' )

    # client host
    parser.add_argument(
        '--client'
        ,action = 'store'
        ,help = 'Host to listen to.'
        ,type = str
        ,default = '127.0.0.1'
    )

    # client Port
    parser.add_argument(
        '--clientport'
        ,action = 'store'
        ,help = 'Port to listen on.'
        ,type = int
        ,default = 2000
    )

    # server host
    parser.add_argument(
        '--server'
        ,action = 'store'
        ,help = 'Host to connect to.'
        ,type = str
        ,default = '127.0.0.1'
    )

    # server Port
    parser.add_argument(
        '--serverport'
        ,action = 'store'
        ,help = 'Port to connect to.'
        ,type = int
        ,default = 2001
    )

    return parser.parse_args()

# Entry poing
if __name__ == "__main__":
    res = main( parseArgs() )
    if ( res != 0 ):
        print( f'main() returned with error: {res}' )