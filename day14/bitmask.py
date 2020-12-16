from typing import List, Tuple
from itertools import product


class BitMask:
    def __init__(self, mask_str: str):
        self._mask_str = mask_str
        self._zeros, self._ones = self._build_masks(mask_str)

    @property
    def mask(self):
        return str(self._mask_str)

    def __repr__(self) -> str:
        return f'BitMask("{self.mask}")'

    def _build_masks(self, mask_str: str) -> Tuple[int, int]:
        zero_bits = int(mask_str.translate(str.maketrans("01X", "100")), base=2)
        one_bits = int(mask_str.translate(str.maketrans("01X", "010")), base=2)
        return zero_bits, one_bits

    def apply(self, number: int) -> int:
        number |= self._ones
        number &= ~self._zeros
        return number

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._mask_str == other._mask_str


class IndexBitMask:
    def __init__(self, mask_str: str):
        self._mask_str = mask_str
        self._ones = int(mask_str.translate(str.maketrans("01X", "010")), base=2)
        self._x_pos = [i for i, chr in enumerate(mask_str) if chr == "X"]
        self._masks = self._generate_masks()

    @property
    def mask(self):
        return str(self._mask_str)

    def __repr__(self) -> str:
        return f'IndexBitMask("{self.mask}")'

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self._mask_str == other._mask_str

    def apply(self, number: int) -> List[int]:
        return [mask.apply(number) for mask in self._masks]

    def _generate_masks(self):
        if len(self._x_pos) == 0:
            masks = [self._bit_mask_from_01_str(self._mask_str)]
        else:
            masks = []
            for ones_and_zeros in product((0, 1), repeat=len(self._x_pos)):
                masks.append(self._generate_mask(ones_and_zeros))
        return masks

    def _generate_mask(self, ones_and_zeros):
        mask_str = list(self._mask_str)
        for pos, val in zip(self._x_pos, ones_and_zeros):
            mask_str[pos] = str(val)
        mask_str = "".join(mask_str)
        return self._bit_mask_from_01_str(mask_str)

    def _bit_mask_from_01_str(self, string: str):
        return BitMask(string.replace("0", "X"))
