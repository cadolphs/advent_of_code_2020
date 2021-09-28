from helpers import get_data
from conway import update_n_steps
from read_input import read_input

def main():
    live_points = read_input(get_data(day=17))

    after_6_steps = update_n_steps(live_points, 6)

    print(f"After 6 steps, there are {len(after_6_steps)} cubes active.")

    live_points = read_input(get_data(day=17), dim=4)
    after_6_steps = update_n_steps(live_points, 6)

    print(f"After 6 steps in four dimensions, there are {len(after_6_steps)} cubes active.")


if __name__ == "__main__":
    main()