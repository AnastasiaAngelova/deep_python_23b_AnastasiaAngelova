import weakref
import timeit
from memory_profiler import profile
from profile_deco import profile_deco


class ClassWithWeakRef:
    def __init__(self, value_set):
        self.value_set = weakref.ref(value_set)


classes = []


@profile_deco
def create_attribute(i):
    return ClassWithWeakRef(set(range(i - 2, i + 3)))


def create_attributes():
    global classes
    classes = [create_attribute(i) for i in range(10_000_000)]


@profile
def get_create_time_attributes():
    return timeit.timeit(create_attributes, number=1)


@profile_deco
def read_attribute(cl):
    return cl.value_set


def read_attributes():
    global classes
    for cl in classes:
        _ = read_attribute(cl)


@profile
def get_access_time_attributes():
    return timeit.timeit(read_attributes, number=1)


get_create_time_attributes()
create_attribute.print_stat()

get_access_time_attributes()
read_attribute.print_stat()
