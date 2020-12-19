from day15.number_game import NumberGame
from helpers import get_data


def main():
    start_numbers = [int(num) for num in get_data(day=15).split(",")]

    number_2020 = NumberGame.get_nth_number(start_numbers, 2020)

    print(f"The 2020th number is {number_2020}")


if __name__ == "__main__":
    main()