class RightCyclicalArray:
    def __init__(self, input_array):
        self._array = input_array

    def __getitem__(self, index):
        if not isinstance(index, tuple):
            raise IndexError(f"{index} is not a valid tuple index")
        col, row = index
        modulo_col = col % self.shape[0] if col > 0 else col

        return self._array[modulo_col, row]

    @property
    def shape(self):
        return self._array.shape
