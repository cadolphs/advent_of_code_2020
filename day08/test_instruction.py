from day08.instruction import (
    AccInstruction,
    Instruction,
    JmpInstruction,
    NopInstruction,
)
from unittest.mock import Mock


def test_load_from_line():
    line = "nop +0"
    instr = Instruction.from_line(line)

    assert isinstance(instr, NopInstruction)


def test_nop_instruction_advances_counter():
    instr = NopInstruction(3)

    computer = Mock()

    instr.execute(computer)

    computer.advance_instruction_pointer.assert_called_with(1)


def test_jmp_instruction_advances_counter():
    instr = JmpInstruction(42)
    computer = Mock()

    instr.execute(computer)

    computer.advance_instruction_pointer.assert_called_with(42)


def test_acc_increases_accumulator():
    instr = AccInstruction(55)
    computer = Mock()

    instr.execute(computer)

    computer.advance_instruction_pointer.assert_called_with(1)
    computer.increase_accumulator.assert_called_with(55)


def test_eq():
    assert AccInstruction(42) == AccInstruction(42)
    assert AccInstruction(55) != AccInstruction(42)
    assert AccInstruction(42) != NopInstruction(42)