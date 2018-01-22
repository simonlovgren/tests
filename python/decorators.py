#!/usr/bin/env python3


# Decorators
def SimpleDecorator( fun ):
    def _SimpleDecorator( name ):
        name = f'my dearest {name}'
        return fun( name )
    return _SimpleDecorator

def ArgDecorator( title ):
    def _ArgDecorator( fun ):
        def __ArgDecorator( name ):
            name = f'my dearest {title} {name}'
            return fun( name )
        return __ArgDecorator
    return _ArgDecorator
            
# Base functions
def printHello( name ):
    print( f'Hello {name}' )

@SimpleDecorator
def printHello2( name ):
    print( f'Hello {name}' )

@ArgDecorator( 'Sir' )
def printHello3( name ):
    print( f'Hello {name}' )

# Normal calls
printHello( 'Anna' )
printHello2( 'Bert' )
printHello3( 'Wolfram' )

# Test 'weird' calls
helloDec = SimpleDecorator( printHello )
helloDec( 'Anna' )

SimpleDecorator( printHello )( 'Herbert' )

ArgDecorator( 'Mr' )( printHello )( 'Simon' )

ArgDecorator( 'Noname Mc.' )( lambda name: print( f'Hello, {name}' ) )( 'Anon' )
