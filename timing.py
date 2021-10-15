import time

def calculate_time():
    """
    This is designed to count the amount of time
    it takes for this specific function to run in seconds.
    """
    initial_time = time.time()
    # Any other actions would go here to get an accurate measurement of how long this function takes.
    final_time = time.time()
    X = final_time - initial_time
    print(f"Total time {X}")

calculate_time()
