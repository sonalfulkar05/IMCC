import threading

def greet():
    print("Hello")
    
t1 = threading.Thread(target=greet) #target is positional arg
t1.run()