from helpers import get_data
from day11.seating_plan import SeatingPlan, SeatingPlan2


def main():
    data = get_data(day=11)

    plan = SeatingPlan.from_string(data)

    final_plan = plan.step_until_stable()

    occupied_seats = final_plan.num_occupied()

    print(f"The stable plan has {occupied_seats} occupied seats.")

    plan_2 = SeatingPlan2.from_string(data)
    final_plan = plan_2.step_until_stable()

    occupied_seats = final_plan.num_occupied()

    print(f"The stable plan has {occupied_seats} occupied seats.")


if __name__ == "__main__":
    main()
