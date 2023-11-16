import timeit
from memory_profiler import profile

classes = []


class ClassWithAttributes:
    def __init__(self, value_set):
        self.value_set = value_set


def create_attributes():
    global classes
    classes = [ClassWithAttributes({j for j in range(i - 2, i + 3)})
               for i in range(10_000_000)]


@profile
def get_create_time_attributes():
    return timeit.timeit(create_attributes, number=1)


def read_attributes():
    global classes

    for cl in classes:
        _ = cl.value_set


@profile
def get_acces_time_attributes():
    return timeit.timeit(read_attributes, number=1)


print(f"time to create: {get_create_time_attributes()} sec")
print("~" * 150)
print(f"time to add elements {get_acces_time_attributes()} sec")
