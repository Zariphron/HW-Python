def parse_input():
    """
    This will take what the user inputs and transform it
    into something the calculator function can recognize.
    """
    user_input = input("Enter equation: ")
    user_input = user_input.split(" ")
    calculator(float(user_input[0]), float(user_input[2]), user_input[1])

def calculator(number1, number2, operator):
    """
    This function will take input from the user and return an output
    based on the user's operation input.

    The operator can be: '+','-','*','/','**', or '//'
    
    """
    result = 0
    if (operator == "+"):
        return result = number1 + number2
    if (operator == "-"):
        return result = number1 - number2
    if (operator == "*"):
        return result = number1 * number2
    if (operator == "/"):
        return result = number1 / number2
    if (operator == "//"):
        return result = number1 // number2
    if (operator == "**"):
        return result = number1 ** number2
    # In the event that the operator variable is not valid, the function will end and give a 'false' output.
    else:
        return False
