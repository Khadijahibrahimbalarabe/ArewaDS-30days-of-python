import math

def calculate_square_root(number):
    if number < 0:
        return "Cannot calculate the square root of a negative number"
    else:
        result = math.sqrt(number)
        return result

# Example usage:
user_input = float(input("Enter a number: "))
result = calculate_square_root(user_input)
print(f"The square root of {user_input} is: {result}")

