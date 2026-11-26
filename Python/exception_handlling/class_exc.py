class InvalidAgeException(Exception):
    pass

try:
    age = 10
    if age < 18:
        raise InvalidAgeException("invalid age")
    
# except ValueError as e:
#     print(e)
finally:
    print("program done!")