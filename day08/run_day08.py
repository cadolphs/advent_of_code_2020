from day08.debugger import Debugger
from helpers import get_data
from day08.computer import Computer, InfiniteLoopException


def main():
    program = get_data(day=8)

    computer = Computer.from_program_string(program)

    try:
        computer.run()
    except InfiniteLoopException:
        pass

    print(f"Computer stopped. Value in accumulator is {computer.accumulator}.")

    print("Let's debug!")

    debugger = Debugger.from_program_string(program)

    debugger.find_candidate_with_no_loop()
    print(f"We fixed it! The output now is {debugger.output}")


if __name__ == "__main__":
    main()
