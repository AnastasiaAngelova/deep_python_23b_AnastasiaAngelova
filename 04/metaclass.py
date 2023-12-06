class CustomMeta(type):
    def __new__(mcs, name, bases, dct):
        new_dict = {}
        for attr_name, attr_value in dct.items():
            if not attr_name.endswith("__"):
                new_dict["custom_" + attr_name] = attr_value
            else:
                new_dict[attr_name] = attr_value

        def __setattr__(self, name, value):
            if name.startswith("custom_"):
                self.__dict__[name] = value
            else:
                self.__dict__["custom_" + name] = value

        new_dict["__setattr__"] = __setattr__
        return super().__new__(mcs, name, bases, new_dict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def __str__(self):
        return "Custom_by_metaclass"

    @staticmethod
    def line():
        return 100
