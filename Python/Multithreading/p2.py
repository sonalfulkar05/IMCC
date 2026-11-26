import threading
import time

def greet():
    time.sleep(3)
    print("Hello")
    
    
def greet2():
    time.sleep(5)
    print("Hello2")
    
    
def greet3():
    print("Hello3")
    
t1 = threading.Thread(target=greet) #target is positional arg
t2 = threading.Thread(target=greet2) 
t3 = threading.Thread(target=greet3) 



t1.start()
t1.join()
t2.start()
t3.start()


print("main program ended")