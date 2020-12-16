class Memory:
    def __init__(self):
        self._memarray = dict()

    def __getitem__(self, index):
        if index < 0 or index >= 2 ** 36:
            raise IndexError("Not a valid index")

        return self._memarray.get(index, 0)

    def __setitem__(self, index, value):
        if index < 0 or index >= 2 ** 36:
            raise IndexError("Not a valid index")
        if value < 0 or value >= 2 ** 36:
            raise ValueError(f"{value} not valid.")
        if index in self._memarray and value == 0:
            del self._memarray[index]
        elif value > 0:
            self._memarray[index] = value

    def items(self):
        return self._memarray.items()

    def keys(self):
        return self._memarray.keys()