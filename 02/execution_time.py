""" HW2 task 2 """
import time


def execution_time(k):
    """ time of func execution for HW2 """

    if not isinstance(k, int):
        raise TypeError("Must be int")
    if k < 1:
        raise ValueError("Must be positive int")

    def decorator(func):
        times = []

        def wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            time_end = time.time()

            if len(times) == k:
                times.pop(0)
            times.append(time_end - time_start)
            print(f"Mean time for last {len(times)} calls: "
                  f"{sum(times) / len(times):.6f} sec")
            return result

        return wrapper

    return decorator
