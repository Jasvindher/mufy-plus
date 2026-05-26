#TODO
#Create a function calculate that takes three arguments:
# - A number
# - An operator (+, -, *, /)
# - Another number
#The function should return the result of the calculation
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
#Test the function with different operations
print(calculate(10, "+", 10))  # Output: 20
print(calculate(10, "-", 10))  # Output: 0
print(calculate(10, "*", 10))  # Output: 100
print(calculate(10, "/", 10))  # Output: 1.0