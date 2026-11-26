age = 5
try:
    if age < 18:
        raise ValueError("you must be 18 or older")
    print("eligible")
except ValueError as e:
    print(e)

else:
    print("access granted")