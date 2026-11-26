try:
    print("Step 1")
    x = int("hello")
    print("Step 2")
    y = 10 / 0
    print("Step 3")
except ValueError:
    print("Value Error Occurred")
except ZeroDivisionError:
    print("Division Error Occurred")

print("Program End")