try:
    num = int(input("enter a number:"))
    result = 100 / num
    print(result)
    
except ValueError as e:
    print(e)
    
except ZeroDivisionError as e:
    print(e)