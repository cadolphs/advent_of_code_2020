class RightCyclicalArray:
    def __init__(self, input_array):
        self._array = input_array

    def __getitem__(self, index):
        if not isinstance(index, tuple):
            raise IndexError(f"{index} is not a valid tuple index")
        row, col = index
        modulo_col = col % self._array.shape[1] if col > 0 else col

        return self._array[row, modulo_col]
