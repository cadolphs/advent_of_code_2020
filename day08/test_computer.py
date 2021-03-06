from day08.instruction import NopInstruction
from day08.computer import Computer, InfiniteLoopException
from unittest.mock import Mock
import pytest


def test_load_from_string_one_line():
    computer = Computer.from_program_string("nop +0")

    assert computer.instruction_pointer == 0


def test_load_from_string_two_line():
    computer = Computer.from_program_string("nop +0\nnop -10")
    assert len(computer._instructions) == 2


def test_simple_run():
    instr = Mock()
    computer = Computer([instr])
    try:
        computer.run()
    except InfiniteLoopException:
        pass

    instr.execute.assert_called_with(computer)


def test_computer_stops_after_coming_to_same_position_twice():
    instr = Mock()
    computer = Computer([instr])
    computer.stop = Mock()
    with pytest.raises(InfiniteLoopException):
        computer.run()


def test_advance_ptr():
    computer = Computer([])

    computer.advance_instruction_pointer(3)

    assert computer.instruction_pointer == 3


def test_computer_runs_one_instr_after_the_other():
    instr_1 = NopInstruction(2)
    instr_2 = Mock()

    computer = Computer([instr_1, instr_1, instr_2])
    try:
        computer.run()
    except InfiniteLoopException:
        pass

    instr_2.execute.assert_called_with(computer)


def test_computer_stops_normally_if_running_over():
    instr = NopInstruction(2)
    computer = Computer([instr, instr])
    computer.stop = Mock()
    computer.run()

    computer.stop.assert_called_once()


def test_increase_accumulator():
    computer = Computer([])

    computer.increase_accumulator(54)
    computer.increase_accumulator(6)

    assert 60 == computer.accumulator
