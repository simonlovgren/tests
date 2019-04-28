#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
UDP Echo server

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

import socket

class EchoServer:
    def __init__( self, port ):
        '''
        Binds to ip/port and listens for data on UDP
        '''
        self.kill = False
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP )
        self.socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        self.socket.setsockopt( socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.settimeout( 0.01 )
        self.socket.bind( ( '', port ) )

    def __del__( self ):
        '''
        Closes socket on deletion of instance
        '''
        self.socket.close()

    def run( self ):
        self.kill = False
        msgCount = 0
        while ( not self.kill ):
            try:
                data, addr = self.socket.recvfrom( 2048 )
                if ( len( data ) > 0 ):
                    print( f'{data}' )
                    msgCount += 1
                    self.socket.sendto( f'[{msgCount:04}] '.encode() + data, addr )
            except socket.timeout as e:
                # Just a timeout
                pass
            except socket.error as e:
                print( f'Socket error: [{e}]' )

    def stop( self ):
        self.kill = True

'''
Only used if called directly
'''
if __name__ == "__main__":
    import signal
    import argparse

    server = None

    def parseargs():
        parser = argparse.ArgumentParser( description = 'UDP echo server.' )

        # remote client to connect to
        parser.add_argument(
            '--port'
            ,action = 'store'
            ,metavar = '<port>'
            ,help = 'Port to listen to.'
            ,type = int
            ,default = '8000'
        )

        return parser.parse_args()    
        pass

    def killHandler( signum, stackFrame ):
        print( f'Shutting down server.' )
        # Signal kill event
        server.stop()

    # Retister SIGTERM and SIGINT handler
    signal.signal( signal.SIGINT, killHandler )
    signal.signal( signal.SIGTERM, killHandler )

    args = parseargs()
    print( f'Listening on port {args.port}' )
    server = EchoServer( args.port )

    server.run()
