def multiply_list(num_List):
    result = 1
    for i in num_List:
        if type(i) == int or float:
            result = result * i
        else:
            False
    result
