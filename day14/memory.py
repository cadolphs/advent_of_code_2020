from day14.bitmask import BitMask


class Memory:
    def __init__(self):
        self._memarray = dict()
        self.mask = BitMask("X" * 36)

    def __getitem__(self, index):
        if index < 0 or index >= 2 ** 36:
            raise IndexError("Not a valid index")

        return self._memarray.get(index, 0)

    def __setitem__(self, index, value):
        masked_value = self.mask.apply(value)
        if index < 0 or index >= 2 ** 36:
            raise IndexError("Not a valid index")
        if masked_value < 0 or masked_value >= 2 ** 36:
            raise ValueError(f"{value} not valid.")
        if index in self._memarray and masked_value == 0:
            del self._memarray[index]
        elif value > 0:
            self._memarray[index] = masked_value

    def items(self):
        return self._memarray.items()

    def keys(self):
        return self._memarray.keys()

    def values(self):
        return self._memarray.values()