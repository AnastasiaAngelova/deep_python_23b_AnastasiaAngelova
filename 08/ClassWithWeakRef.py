import weakref
import timeit
from memory_profiler import profile

classes = []


class ClassWithWeakRef:
    def __init__(self, value_set):
        self.value_set = weakref.ref(value_set)


def create_slots():
    global classes
    classes = [ClassWithWeakRef({j for j in range(i - 2, i + 3)})
               for i in range(10_000_000)]


@profile
def get_create_time_slots():
    return timeit.timeit(create_slots, number=1)


def read_slots():
    global classes

    for cl in classes:
        _ = cl.value_set


@profile
def get_acces_time_slots():
    return timeit.timeit(read_slots, number=1)


print(f"time to create: {get_create_time_slots()} sec")
print("~" * 150)
print(f"time to add elements {get_acces_time_slots()} sec")
