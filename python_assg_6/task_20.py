# 20. Creating a Custom Exception
# Assignment: Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception 
# if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)