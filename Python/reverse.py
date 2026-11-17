a = 1234
reverse = 0
while a > 0:
    last = a % 10
    reverse = reverse * 10 + last
    a = a // 10
print("Reversed number:", reverse)
 
square = [x*x for x in range(1,6)]
print(square)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
print(fact(5))

print(type(10//2))
print(bool([2]))
print('Python'[1:4])
print(len({'a':1, 'b':2}))
print((lambda x: x+3)(4))
print([1, 2] + [3])

print(type(-2))