#!/usr/bin/env python3

import socket, threading, pickle, sys


################################################################################
# Message content classes
################################################################################

class Message( object ):
    def __init__( self, message ):
        super().__init__();
        self.message = message

    def GetMessage( self ):
        return self.message
        
class Event( object ):
    def __init__( self ):
        super().__init__();
        self.event = 0
        self.description = ''

    def SetDescription( self, descr ):
        self.description = descr

    def SetEvent( self, event ):
        self.event = event

    def GetDescription( self ):
        return self.description

    def GetEvent( self ):
        return self.event

################################################################################
# Server
################################################################################

class Server( object ):
    def __init__( self, host, port ):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = None
        self.app    = None
        self.threads = []
        self.run     = False
        
    def __exit__( self ):
        self.Stop()

    def SetApplication( self, app ):
        if not self.socket:
            self.app = app
        else:
            print( 'Server is running. Please stop it before changing main application.' )
            
    def Start( self ):
        self.run = True
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.socket.bind( (self.host, self.port) )
        #self.socket.settimeout(1)
        self.socket.listen(1)

        try:
            while True:
                print( f'Waiting for connection on {self.host}:{self.port}' )
                conn, addr = self.socket.accept()
                print( f'Connection from {addr}' )
                thread = threading.Thread(
                    target = self.HandleConnection,
                    args   = (conn, addr)
                )
                self.threads.append(thread)
                thread.start()
        except KeyboardInterrupt:
            print( 'KeyboardInterrupt, stopping server' )
        finally:
            self.Stop()

    def HandleConnection( self, client, address ):
        size = 1024
        app = self.DefaultApp
        if self.app:
            app = self.app
        client.settimeout(1)
        while self.run:
            try:
                data = client.recv( size )
                if data:
                    response = app( data )
                    if response:
                        client.sendall( response )
                else:
                    raise Exception( 'Client disconnected' )
            except socket.timeout as to:
                #print( 'No message in the last second, time to check if i shall die or not...' )
                pass
            except:
                print( f'[{address}] disconnected!' )
                client.close()
                return False
            
    def Stop( self ):
        # Inform threads to die
        self.run = False
        for i,thread in enumerate(self.threads):
            print( f'Waiting for thread {i}' )
            thread.join()
        if self.socket:
            print( 'Closing socket...')
            self.socket.close()
        self.threads = []
        
    def DefaultApp( self, data ):
        # Simple print-and-return
        print(data.decode())
        return data

################################################################################
# Client
################################################################################

class Client( object ):
    def __init__( self, host, port ):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = None

    def __exit__( self ):
        self.Disconnect()

    def Connect( self ):
        print( f'Connecting to {self.host}:{self.port}')
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.socket.connect( (self.host, self.port) )

    def Disconnect( self ):
        if self.socket:
            self.socket.close()

    def Send( self, data ):
        if self.socket:
            self.socket.sendall( data )

    def Receive( self ):
        return self.socket.recv( 1024 )


################################################################################
# Custom app
################################################################################
def MyApp( data ):
    # Data is pickled, unpickle
    msg = pickle.loads( data )
    if isinstance( msg, Event ):
        print( 'Event got!' )
    elif isinstance( msg, Message ):
        print( 'Message get!' )
        print( msg.GetMessage() )
        
################################################################################
# Command line stuff
################################################################################

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 's':
            server = Server( 'localhost', 10000 )
            server.SetApplication(MyApp)
            server.Start()
        elif sys.argv[1] == 'c':
            client = Client( 'localhost', 10000 )
            try:
                client.Connect()
                while True:
                    data = None
                    t = input('Type (m/e): ')
                    if t == 'e':
                        data = Event()
                    else:
                        msg = input('Message: ')
                        data = Message( msg )
                    client.Send( pickle.dumps(data) )
            except KeyboardInterrupt:
                print()
                print( 'Client shutdown' )
                client.Disconnect()
    else:
        print( f'Usage:  {sys.argv[0]} [s][c]' )
