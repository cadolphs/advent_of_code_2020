from typing import Tuple


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
