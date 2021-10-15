def multiply_list(num_List):
    """
    This will take in a list and multiply
    each number by the previous number in the list
    continuously until it reaches the end of the list.

    The end result will be all numbers multiplied together.

    Example:
    [2,3,4]
    Because 2*3*4
    Will end up being = 24

    """
    result = 1
    # The result cannot be non-initialized otherwise it will return an error.
    for i in num_List:
        if type(i) == int or float:
            result = result * i
        else:
            return False
    return result

"""def parse_input():
    user_numbers = []
    string_input = input("Input = ")
    string_input = string_input.replace("[", "")
    string_input = string_input.replace("]", "")
    string_input = string_input.split(",")
    for i in string_input:
        user_numbers.append(int(i))
    multiply_list(user_numbers)
"""
