from day08.instruction import parse_program_to_instructions
from day08.debugger import Debugger, generate_candidate_programs


def test_finds_infinite_loop():
    program_with_loop = "jmp +0"

    debugger = Debugger.from_program_string(program_with_loop)

    assert debugger.has_infinite_loop(debugger._original_instructions)


def test_knows_when_there_is_no_loop():
    program_without_loop = "jmp +2\nnop +0\nnop +3\nacc +5"

    debugger = Debugger.from_program_string(program_without_loop)

    assert not debugger.has_infinite_loop(debugger._original_instructions)


def test_generate_candidate_leaves_acc_alone():
    program = "acc +44"
    instructions = parse_program_to_instructions(program)

    candidates = list(generate_candidate_programs(instructions))

    assert 0 == len(candidates)


def test_generate_single_candidate():
    program = "acc +44\nnop +2\nacc +2"

    instructions = parse_program_to_instructions(program)

    expected_program = "acc +44\njmp +2\nacc +2"
    expected_instructions = parse_program_to_instructions(expected_program)

    candidates = list(generate_candidate_programs(instructions))

    assert 1 == len(candidates)
    assert expected_instructions == candidates[0]


def test_generate_two_candidates():
    """Actually a super helpful test to figure out the copy and mutability stuff..."""
    program = "nop +2\njmp +1\nacc +5"

    instructions = parse_program_to_instructions(program)

    expected_program_1 = "jmp +2\njmp +1\nacc +5"
    expected_program_2 = "nop +2\nnop +1\nacc +5"

    expected_instructions_1 = parse_program_to_instructions(expected_program_1)
    expected_instructions_2 = parse_program_to_instructions(expected_program_2)

    candidates = list(generate_candidate_programs(instructions))

    assert 2 == len(candidates)
    assert expected_instructions_1 == candidates[0]
    assert expected_instructions_2 == candidates[1]


def test_test_input():
    program = """   nop +0
                    acc +1
                    jmp +4
                    acc +3
                    jmp -3
                    acc -99
                    acc +1
                    jmp -4
                    acc +6"""

    debugger = Debugger.from_program_string(program)

    fixed_program = debugger.find_candidate_with_no_loop()

    fixed_program_str = """ nop +0
                            acc +1
                            jmp +4
                            acc +3
                            jmp -3
                            acc -99
                            acc +1
                            nop -4
                            acc +6"""

    fixed_instructions = parse_program_to_instructions(fixed_program_str)

    assert fixed_instructions == fixed_program
    assert debugger.output == 8