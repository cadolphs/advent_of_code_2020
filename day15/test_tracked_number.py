from day15.tracked_number import TrackedNumber


def test_saying_a_number_once_causes_0_to_be_said():
    number = TrackedNumber()

    number.say(turn=1)

    assert 0 == number.get_number_to_say()


def test_saying_a_number_a_couple_of_times_causes_difference_to_be_said():

    number = TrackedNumber()

    number.say(turn=1)
    number.say(turn=42)

    assert 41 == number.get_number_to_say()