import threading, time, argparse

killEvent = threading.Event()
printLock = threading.Lock()
startTime = time.time()

def tsPrint( tId, msg ):
    printLock.acquire()
    elapsedTime = time.time() - startTime
    print( f'[{elapsedTime:05.1f}][{tId}] {msg}' )
    printLock.release()

class MyThread( threading.Thread ):
    def __init__( self, tId ):
        super().__init__()
        self.id = tId

    def run( self ):
        time.sleep(1)
        while( not killEvent.is_set() ):
            tsPrint( self.id, f'Thread reporting!' )
            time.sleep( 1 )
        tsPrint( self.id, 'Kill event, thread exiting!' )

def main( args ):
    threads = range( 0,args.threads )
    threadList = []

    # Spin up threads
    tsPrint( 'main', f'Starting threads.' )
    for t in threads:
        thread = MyThread( t )
        thread.start()
        threadList.append( thread )

    # Wait for user to choose exit
    tsPrint( 'main', 'Press <ENTER> to kill threads and exit.' )
    input()

    # Signal kill event
    killEvent.set()

    # Wait for threads to die
    for t in threadList:
        t.join()

    # All threads exited
    tsPrint( 'main', 'All threads exited, exiting program!' )
    return 0


def parseArgs():
    parser = argparse.ArgumentParser( description = 'Multithreaded TCP server.' )

    # Number of threads
    parser.add_argument(
        'threads'
        ,action = 'store'
        ,help = 'Number of threads to start.'
        ,type = int
        ,default = 3
    )

    return parser.parse_args()

# Entry poing
if __name__ == '__main__':
    res = main( parseArgs() )
    if ( res != 0 ):
        print( f'main() returned with error: {res}' )