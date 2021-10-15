

def tripler_recurse(function, count):
    """
    This function will take a function
    and perform that function three times before stopping.
    """
    caller_count = count + 1
    if (caller_count == 4):
        return
    else:
        print(f"Count: {caller_count} func: {function}")
        return tripler_recurse(function, caller_count)

def tripler(func_call):
    return tripler_recurse(func_call, 0)
