from day14.bitmask import IndexBitMask
from day14.runner import Runner
from day14.memory import FloatingMemory, Memory
from helpers import get_data


def main():
    commands = [line for line in get_data(day=14).split("\n")]

    memory = Memory()
    runner = Runner(memory)

    for command in commands:
        runner.execute(command)

    sum_of_all_values = sum(memory.values())

    print(f"Sum of all values is {sum_of_all_values}")

    new_memory = FloatingMemory()
    new_runner = Runner(new_memory, mask_factory=IndexBitMask)

    for command in commands:
        new_runner.execute(command)

    sum_of_all_values = sum(new_memory.values())

    print(f"Sum of all values in new memory is {sum_of_all_values}")


if __name__ == "__main__":
    main()