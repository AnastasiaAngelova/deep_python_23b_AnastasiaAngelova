""" HW2 task 2 """

import time
from functools import wraps


def execution_time(k):
    """ time of func execution for HW2 """
    times = []

    if not isinstance(k, int):
        raise TypeError("Must be int")
    if k < 1:
        raise ValueError("Must be positive int")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            time_end = time.time()
            times.append(time_end - time_start)
            if len(times) == k:
                print(f"Mean time for last {k} calls: "
                      f"{sum(times) / len(times):.6f} sec")
                times.clear()
            return result
        return wrapper
    return decorator
