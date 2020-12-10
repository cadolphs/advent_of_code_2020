from day08.computer import Computer, InfiniteLoopException


def main():
    # Now we create a super simple program of just one line doing nothing.
    prog = "nop +0"

    computer = Computer.from_program_string(prog)
    computer.run()

    assert 0 == computer.accumulator
    assert 1 == computer.instruction_pointer

    print("All okay so far.")

    another_prog = "nop +0\nnop -10"
    computer = Computer.from_program_string(another_prog)

    computer.run()

    assert 2 == computer.instruction_pointer

    # Now for the big one!
    prog = """  nop +0
                acc +1
                jmp +4
                acc +3
                jmp -3
                acc -99
                acc +1
                jmp -4
                acc +6"""

    computer = Computer.from_program_string(prog)

    try:
        computer.run()
    except InfiniteLoopException:
        pass

    print(f"Program stopped. Value in accumulator is {computer.accumulator}")


if __name__ == "__main__":
    main()
