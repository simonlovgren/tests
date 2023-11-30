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
import time

class EchoServer:
    def __init__( self, ip, port, speedOnly ):
        '''
        Binds to ip/port and listens for data on UDP
        '''
        self.kill = False
        self.speedOnly = speedOnly
        self.socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        self.socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        self.socket.settimeout( 0.01 )
        self.socket.bind( ( ip, port ) )
        self.lastPacket = 0

    def __del__( self ):
        '''
        Closes socket on deletion of instance
        '''
        self.socket.close()

    def run( self ):
        self.kill = False
        maxspeed = 0
        toofast  = False
        while ( not self.kill ):
            try:
                data, addr = self.socket.recvfrom( 2048 )
                if ( len( data ) > 0 ):
                    if ( self.speedOnly ):
                        currentTimestamp = time.time()
                        if ( self.lastPacket > 0 ):
                            delta = currentTimestamp - self.lastPacket
                            if ( delta > 0 ):
                                bps   = ( len( data ) * 8 ) / delta
                                if ( bps > maxspeed ):
                                    maxspeed = bps
                                print( f'{round( maxspeed )} b/s max measured', end = '\r' )
                            else:
                                if ( toofast == False ):
                                    print( 'Too fast for measurement...' )
                                    toofast = True

                        self.lastPacket = currentTimestamp
                    else:
                        print( f'{data}' )
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

        # client port
        parser.add_argument(
            '--ip'
            ,action = 'store'
            ,metavar = '<ip>'
            ,help = 'IP to listen on.'
            ,type = str
            ,default = '0.0.0.0'
        )

        # remote client to connect to
        parser.add_argument(
            '--port'
            ,action = 'store'
            ,metavar = '<port>'
            ,help = 'Port to listen to.'
            ,type = int
            ,default = '8000'
        )

        parser.add_argument(
            '--speed'
            ,action = 'store_true'
            ,help   = 'Only print speed of incoming data'
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
    print( f'Listening on {args.ip}, port {args.port}' )
    server = EchoServer( args.ip, args.port, args.speed )

    server.run()
