from day11.seating_plan import SeatingPlan, SeatingPlan2


def test_from_string():
    data = ".L.\n#.L\n..."

    plan = SeatingPlan.from_string(data)

    assert 1 == plan.num_occupied()

    # What other _questions_ would I ask from the seating plan to make sure it works...?
    # Currently not much!


def test_flip_rule_nothing_occupied():
    data = ".L.\n..L\n..."

    plan = SeatingPlan.from_string(data)

    new_plan = plan.step()

    expected_plan = SeatingPlan.from_string(".#.\n..#\n...")

    assert expected_plan == new_plan


def test_flip_rule_four_occupied():
    data = "#.#\n.#.\n#.#"
    plan = SeatingPlan.from_string(data)

    new_plan = plan.step()

    expected_plan = SeatingPlan.from_string("#.#\n.L.\n#.#")

    assert expected_plan == new_plan


def test_eq():
    data = ".L.\n#.L\n..."

    plan = SeatingPlan.from_string(data)
    nother_plan = SeatingPlan.from_string(data)

    assert plan == nother_plan


def test_example_input_part1():
    input_seating = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"
    first_step = input_seating.replace("L", "#")
    second_step = "#.LL.L#.##\n#LLLLLL.L#\nL.L.L..L..\n#LLL.LL.L#\n#.LL.LL.LL\n#.LLLL#.##\n..L.L.....\n#LLLLLLLL#\n#.LLLLLL.L\n#.#LLLL.##"
    third_step = "#.##.L#.##\n#L###LL.L#\nL.#.#..#..\n#L##.##.L#\n#.##.LL.LL\n#.###L#.##\n..#.#.....\n#L######L#\n#.LL###L.L\n#.#L###.##"
    fourth_step = "#.#L.L#.##\n#LLL#LL.L#\nL.L.L..#..\n#LLL.##.L#\n#.LL.LL.LL\n#.LL#L#.##\n..L.L.....\n#L#LLLL#L#\n#.LLLLLL.L\n#.#L#L#.##"
    fifth_step = "#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##"

    first_plan = SeatingPlan.from_string(input_seating)
    second_plan = SeatingPlan.from_string(first_step)
    third_plan = SeatingPlan.from_string(second_step)
    fourth_plan = SeatingPlan.from_string(third_step)
    fifth_plan = SeatingPlan.from_string(fourth_step)
    sixth_plan = SeatingPlan.from_string(fifth_step)

    assert second_plan == first_plan.step()
    assert third_plan == second_plan.step()
    assert fourth_plan == third_plan.step()
    assert fifth_plan == fourth_plan.step()
    assert sixth_plan == fifth_plan.step()


def test_find_repeater():
    input_seating = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"
    stable_seating = "#.#L.L#.##\n#LLL#LL.L#\nL.#.L..#..\n#L##.##.L#\n#.#L.LL.LL\n#.#L#L#.##\n..L.L.....\n#L#L##L#L#\n#.LLLLLL.L\n#.#L#L#.##"

    plan = SeatingPlan.from_string(input_seating)
    stable_plan = SeatingPlan.from_string(stable_seating)

    final_plan = plan.step_until_stable()

    assert final_plan == final_plan.step()
    assert stable_plan == final_plan


def test_2_step():
    input_seating = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"
    third_seating = "#.LL.LL.L#\n#LLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLL#\n#.LLLLLL.L\n#.LLLLL.L#"

    plan = SeatingPlan2.from_string(input_seating)
    first_plan = plan.step()
    next_plan = first_plan.step()

    expected = SeatingPlan2.from_string(third_seating)

    assert expected == next_plan
