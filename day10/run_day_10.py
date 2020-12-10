from typing import List
from collections import Counter
from helpers import get_data


def main():
    data = get_data(day=10).split("\n")
    input_joltages = [int(line) for line in data]

    joltage_chain = make_joltage_chain(input_joltages)
    counter = count_joltage_diffs(joltage_chain)

    answer = counter[1] * counter[3]

    print(f"The product of 1 and 3 diff steps is {answer}")

    num_paths = count_joltage_paths(joltage_chain)

    print(f"There are {num_paths} different arrangements you could make!")


def make_joltage_chain(joltages: List[int]) -> List[int]:
    port = 0
    built_in = max(joltages) + 3

    new_list = [port]
    new_list.extend(sorted(joltages))
    new_list.append(built_in)

    return new_list


def count_joltage_diffs(joltages: List[int]) -> Counter:
    # Could use numpy here but zip works too.
    diffs = (right - left for (left, right) in zip(joltages, joltages[1:]))

    counter = Counter(diffs)

    return counter


def count_joltage_paths(joltages: List[int]) -> int:
    """Assumes that `joltages` is sorted!"""

    # We make this a bit larger than you'd think so that the lookups still work!
    num_paths = [0] * (max(joltages) + 3)
    num_paths[joltages[-1]] = 1

    for joltage in reversed(joltages[:-1]):
        num_paths[joltage] = sum(num_paths[joltage + i] for i in (1, 2, 3))

    return num_paths[0]


if __name__ == "__main__":
    main()