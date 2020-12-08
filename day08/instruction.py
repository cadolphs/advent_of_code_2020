from day08.parse_data import parse_line


class Instruction:
    def __init__(self, arg):
        self._arg = arg

    @property
    def arg(self):
        return self._arg

    @staticmethod
    def from_line(line: str) -> "Instruction":
        """Note: In _general_ switching on type or type codes is a code smell.
        The one exception is factory methods / factory classes. This is the _only_
        place in the whole program where we switch on the operator code; everywhere
        else we rely on polymorphism."""
        op, arg = parse_line(line)

        if op == "nop":
            return NopInstruction(arg)
        elif op == "acc":
            return AccInstruction(arg)
        elif op == "jmp":
            return JmpInstruction(arg)

        raise NotImplementedError("We will get to there")

    def execute(self, computer):
        computer.increase_accumulator(self.accumulator_increment())
        computer.advance_instruction_pointer(self.instruction_step())

    # Override these in child classes:

    def instruction_step(self):
        return 1

    def accumulator_increment(self):
        return 0


class NopInstruction(Instruction):
    pass


class JmpInstruction(Instruction):
    def instruction_step(self):
        return self.arg


class AccInstruction(Instruction):
    def accumulator_increment(self):
        return self.arg
