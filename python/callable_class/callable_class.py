

class MyClass( object ):

    def __init__( self ):
        if not __class__.__name__ == self.__class__.__name__:
            print(f"[{__class__.__name__}] Initialized by [{self.__class__.__name__}]")
        else:
            print(f"[{__class__.__name__}] Initialized")

    def myMethod( self ):
        print(f"[{self.__class__.__name__}] myMethod was called")

class MyCallableClass( MyClass ):

    def __init__( self ):
        print(f"[{__class__.__name__}] initialized")
        super(MyCallableClass, self).__init__()

    def __call__( self ):
        print(f"[{self.__class__.__name__}] I a an class was called!")

if __name__ == '__main__':
    mc = MyClass()
    mc.myMethod()

    mcc = MyCallableClass()
    mcc.myMethod()
    mcc()