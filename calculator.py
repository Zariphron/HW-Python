def parse_input():
    user_input = input("Enter equation: ")
    user_input = user_input.split(" ")
    calculator(float(user_input[0]), float(user_input[2]), user_input[1])

def calculator(number1, number2, operator):
    result = 0
    if (operator == "+"):
        result = number1 + number2
    if (operator == "-"):
        result = number1 - number2
    if (operator == "*"):
        result = number1 * number2
    if (operator == "/"):
        result = number1 / number2
    if (operator == "//"):
        result = number1 // number2
    if (operator == "**"):
        result = number1 ** number2
    else:
        False

parse_input()
