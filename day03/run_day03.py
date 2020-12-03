from day03.positions import positions
from day03.right_cyclical_array import RightCyclicalArray
from day03.map_parser import parse_map
from helpers import get_data

from day01.expense_check import product


def count_trees(tree_map, positions):
    return sum(1 for pos in positions if tree_map[pos])


def count_trees_for_direction(tree_map, direction):
    max_rows = tree_map.shape[1]
    pos_to_check = positions((0, 0), direction, max_rows)

    return count_trees(tree_map, pos_to_check)


def main():
    data = get_data(day=3)

    tree_map = RightCyclicalArray(parse_map(data))

    pos_to_check = positions((0, 0), (3, 1), tree_map.shape[1])

    num_trees = count_trees(tree_map, pos_to_check)

    print(f"For direction (3, 1) we encounter {num_trees} trees.")

    all_directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    all_tree_prod = product(
        count_trees_for_direction(tree_map, direction) for direction in all_directions
    )

    print(f"Product of all tree numbers is {all_tree_prod}")


if __name__ == "__main__":
    main()
