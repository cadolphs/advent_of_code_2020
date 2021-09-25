class Rule:
    def __init__(self, name: str, range1: (int, int), range2: (int, int)):
        self.name = name
        self.range1 = range1
        self.range2 = range2

    def is_valid(self, value: int) -> bool:
        return self.range1[0] <= value <= self.range1[1] or self.range2[0] <= value <= self.range2[1]

    def is_valid_vectorized(self, value):
        return ((self.range1[0] <= value) & (value <= self.range1[1])) | ((self.range2[0] <= value) & (value <= self.range2[1]))

    def __str__(self):
        return f"{self.name}: {self.range1[0]}-{self.range1[1]} or {self.range2[0]}-{self.range2[2]}"

    def __repr__(self):
        return f'Rule("{self.name}", {self.range1!r}, {self.range2!r}'
    