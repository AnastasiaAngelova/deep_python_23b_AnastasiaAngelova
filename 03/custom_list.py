class CustomList(list):
    def __str__(self):
        return " ".join([str(x) for x in self]) + " sum=" + str(len(self))

    def __add__(self, other):
        list_add = CustomList()
        for i in range(min(len(self), len(other))):
            list_add.append(self[i] + other[i])
        if len(self) > len(other):
            for i in range(len(other), len(self)):
                list_add.append(self[i])
        elif len(self) < len(other):
            for i in range(len(self), len(other)):
                list_add.append(other[i])
        return list_add

    def __radd__(self, other):
        return CustomList.__add__(other, self)

    def __sub__(self, other):
        list_add = CustomList()
        for i in range(min(len(self), len(other))):
            list_add.append(self[i] - other[i])
        if len(self) > len(other):
            for i in range(len(other), len(self)):
                list_add.append(self[i])
        elif len(self) < len(other):
            for i in range(len(self), len(other)):
                list_add.append(-other[i])
        return list_add

    def __rsub__(self, other):
        return CustomList.__sub__(other, self)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
