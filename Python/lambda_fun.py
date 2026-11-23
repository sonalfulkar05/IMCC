def lam_fun():
    # Lambda function to add two numbers
    add = lambda x, y: x + y
    print("Sum:", add(5, 3))

    # Lambda function to square a number
    square = lambda x: x * x
    print("Square:", square(4))

    # Lambda function to check if a number is even
    is_even = lambda x: x % 2 == 0
    print("Is 6 even?", is_even(6))
print("Lambda Function Examples:")
lam_fun()
