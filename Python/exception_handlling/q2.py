print("program is starting...")

try:
    num = int(input("enter a number:"))
    result = 100 / num
    print(result)
    
except ValueError as e:
    print(e)
    
except ZeroDivisionError as e:
    print(e)
    
else:
    print("program excecuted successfully")
    
finally:
    print("this is mandatory block,it'll excecute whatever the condition is. ")