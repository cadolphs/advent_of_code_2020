from day14.bitmask import BitMask, IndexBitMask


class SpecialSetMemory:
    def __init__(self) -> None:
        self._memarray = dict()

    def __getitem__(self, index):
        if index < 0 or index >= 2 ** 36:
            raise IndexError("Not a valid index")

        return self._memarray.get(index, 0)

    def items(self):
        return self._memarray.items()

    def keys(self):
        return self._memarray.keys()

    def values(self):
        return self._memarray.values()

    def set_at_raw(self, index, value):
        if index < 0 or index >= 2 ** 36:
            raise IndexError("Not a valid index")
        if index in self._memarray and value == 0:
            del self._memarray[index]
        elif value > 0:
            self._memarray[index] = value


class Memory(SpecialSetMemory):
    def __init__(self):
        super().__init__()
        self.mask = BitMask("X" * 36)

    def __setitem__(self, index, value):
        masked_value = self.mask.apply(value)

        if masked_value < 0 or masked_value >= 2 ** 36:
            raise ValueError(f"{value} not valid.")

        self.set_at_raw(index, masked_value)


class FloatingMemory(SpecialSetMemory):
    def __init__(self) -> None:
        super().__init__()
        self.mask = IndexBitMask("0" * 36)

    def __setitem__(self, index, value):
        if value < 0 or value >= 2 ** 36:
            raise ValueError(f"{value} not valid.")

        for masked_index in self.mask.apply(index):
            self.set_at_raw(masked_index, value)
