from day14.bitmask import BitMask
import regex as re

mask_regex = re.compile(r"mask = (?P<mask>[01X]+)")
memset_regex = re.compile(r"mem\[(?P<index>\d+)\] = (?P<value>\d+)")


class Runner:
    def __init__(self, memory, mask_factory=BitMask):
        self.memory = memory
        self._mask_factory = mask_factory

    def execute(self, command: str):
        if match_group := mask_regex.match(command):
            mask_str = match_group.group("mask")
            self.memory.mask = self._mask_factory(mask_str)
        elif match_group := memset_regex.match(command):
            index = int(match_group.group("index"))
            value = int(match_group.group("value"))

            self.memory[index] = value
