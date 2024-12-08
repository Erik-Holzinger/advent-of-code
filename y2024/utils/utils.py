import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time_s = (end_time - start_time)
        elapsed_time_ms = (end_time - start_time) * 1000
        print(f"Result of {func.__name__} is {result} and took {elapsed_time_s:.2f} seconds ({elapsed_time_ms:.2f} ms)")
        return result

    return wrapper
