#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Main entrypoint for UDP chat test.

'''

'''
MIT License

Copyright (c) 2019 Simon Lövgren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import argparse
import socket
import threading
import signal

globalStop = threading.Event()

class EchoClient():
    def __init__( self, ip, port ):
        self.ip = ip
        self.port = port

        # Socket
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        self.socket.settimeout( 0.01 )

        # Recv-thread
        self.receive_thread = threading.Thread( target = self._receive_thread )
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def _receive_thread( self ):
        while ( not globalStop.is_set() ):
            try:
                data, addr = self.socket.recvfrom( 2048 )
                if ( len( data ) > 0 ):
                    print( f'-> {data}' )
            except socket.timeout as e:
                # Just a timeout
                pass
            except socket.error as e:
                print( f'Socket error: [{e}]' )

    def run( self ):
        while( not globalStop.is_set() ):
            try:
                data = input()
                self.socket.sendto( data.encode(), ( self.ip, self.port ) )
            except socket.error as e:
                print( f'Socket error: [{e}]' )
            except EOFError as e:
                pass






'''
Command line stuff
'''

def killHandler( signum, stackFrame ):
    print( f'Exiting.' )
    # Signal kill event
    globalStop.set()

def main( remote ):
    print( f'Sending to {remote.split(":")[0]}, port {remote.split(":")[1]}')

    # Register SIGTERM and SIGINT handler
    signal.signal( signal.SIGINT, killHandler )
    signal.signal( signal.SIGTERM, killHandler )

    client = EchoClient( remote.split(":")[0], int( remote.split(":")[1] ) )
    client.run()

def parseargs():
    parser = argparse.ArgumentParser( description = 'UDP Chat client.' )

    # remote client to connect to
    parser.add_argument(
        '--remote'
        ,action = 'store'
        ,metavar = '<host>:<port>'
        ,help = 'Client to connect to.'
        ,type = str
        ,default = '127.0.0.1:8000'
    )

    return parser.parse_args()    
    pass

if __name__ == "__main__":
    args = parseargs()
    main(
        args.remote
    )