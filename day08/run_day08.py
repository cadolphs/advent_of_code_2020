from helpers import get_data
from day08.computer import Computer


def main():
    program = get_data(day=8)

    computer = Computer.from_program_string(program)

    computer.run()

    print(f"Computer stopped. Value in accumulator is {computer.accumulator}.")


if __name__ == "__main__":
    main()