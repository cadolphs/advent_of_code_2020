from day08.instruction import (
    Instruction,
    JmpInstruction,
    NopInstruction,
    parse_program_to_instructions,
)
from typing import Iterable, Iterator, List
from day08.computer import Computer, InfiniteLoopException


class Debugger:
    def __init__(self, instructions: Iterable[Instruction]):
        self._original_instructions = list(instructions)
        self._output = None

    def has_infinite_loop(self, instructions: Iterable[Instruction]) -> bool:
        computer = self._make_computer(instructions)
        try:
            computer.run()
            self._output = computer.accumulator
        except InfiniteLoopException:
            return True
        return False

    def find_candidate_with_no_loop(self):
        for candidate in generate_candidate_programs(self._original_instructions):
            if not self.has_infinite_loop(candidate):
                return candidate
        raise ValueError("None of the bugfix attempts worked! Everything runs forever.")

    @property
    def output(self):
        return self._output

    @classmethod
    def _make_computer(cls, instructions: Iterable[Instruction]) -> Computer:
        """Might look redundant. We are encapsulating class creation in case we later want to refactor"""
        return Computer(instructions)

    @classmethod
    def from_program_string(cls, program: str) -> "Debugger":
        instructions = parse_program_to_instructions(program)

        debugger = cls(instructions)
        return debugger


def generate_candidate_programs(instructions: List[Instruction]) -> Iterator:
    def _have_to_adjust(instruction):
        """Normally type switches are code smells. Here we're doing "debugging". It is not
        reasonable to expect that the NopInstruction itself is responsible for knowing that
        we want to try changing it into a JmpInstruction!"""
        return isinstance(instruction, NopInstruction) or isinstance(
            instruction, JmpInstruction
        )

    def _adjust(instruction):
        if isinstance(instruction, NopInstruction):
            return JmpInstruction(instruction.arg)
        elif isinstance(instruction, JmpInstruction):
            return NopInstruction(instruction.arg)

    def _revert(instruction):
        return _adjust(
            instruction
        )  # Currently reverting the adjustment means repeating it.

    local_instructions = list(instructions)
    for i, instruction in enumerate(local_instructions):
        if _have_to_adjust(instruction):
            local_instructions[i] = _adjust(instruction)
            yield list(local_instructions)
            local_instructions[i] = _revert(local_instructions[i])
