import socket
import sys

# Create a TCP/IP socket
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

# Bind the socket to the port
address = '127.0.0.1'
port    = 10021
server_address = ( address, port )
print( 'Server listening on {address}:{port}' )
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print( 'Waiting for connection' )
    client, address = sock.accept()
    try:
        print('connection from', address)
        # Read data from client and echo back
        while True:
            data = client.recv( 1024 )
            print( f'received {data}' )
            if data:
                # Echo back to client
                client.sendall( data )
            else:
                print( 'Client disconnected' )
                break
    finally:
        client.close()