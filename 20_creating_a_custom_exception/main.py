class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

try:
    age = 18
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")