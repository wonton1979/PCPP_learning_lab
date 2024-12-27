from datetime import datetime

def show_running_time(func):
    def wrapper(n):
        start_time = datetime.now()
        func(n)
        end_time = datetime.now()
        print(f"Running {func.__name__} in {(end_time - start_time).microseconds} microseconds which equal to {(end_time - start_time).seconds} seconds.")
    return wrapper

@show_running_time
def factorial(n):
    total = 1
    for i in range(2, n + 1):
        total *= i


factorial(100000)