from typing import Iterable
from day08.instruction import Instruction


class Computer:
    def __init__(self, instructions: Iterable[Instruction]):
        self._accumulator = 0
        self._instr_ptr = 0
        self._instructions = list(instructions)

    @property
    def accumulator(self):
        return self._accumulator

    @property
    def instruction_pointer(self):
        return self._instr_ptr

    def advance_instruction_pointer(self, offset: int):
        self._instr_ptr += offset

    def increase_accumulator(self, incr: int):
        self._accumulator += incr

    def run(self):
        positions_visited = set()

        try:
            while self.instruction_pointer not in positions_visited:
                positions_visited.add(self.instruction_pointer)
                instr = self._load_instruction()
                instr.execute(self)
        except StopExecution:
            pass

        self.stop()

    def _load_instruction(self):
        try:
            return self._instructions[self.instruction_pointer]
        except IndexError:
            print("Index out of bound. Stopping for now!")
            raise StopExecution()

    def stop(self):
        pass

    @classmethod
    def from_program_string(cls, program: str) -> "Computer":
        instructions = [Instruction.from_line(line) for line in program.split("\n")]
        return cls(instructions)


class BufferOverrunError(Exception):
    pass


class StopExecution(Exception):
    pass