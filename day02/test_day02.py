from day02.password_checker import (
    is_password_valid,
    is_password_valid_v2,
    InputLine,
    parse_input_line,
    count_valid,
)


def test_single_check_password():
    low, high = (1, 3)
    letter = "a"
    password = "abcde"

    assert is_password_valid(low, high, letter, password)

    assert not is_password_valid(1, 3, "b", "cdefg")


def test_parse_input_line():
    line = "1-3 a: abcde"

    parsed_result = parse_input_line(line)

    expected_result = InputLine(1, 3, "a", "abcde")

    assert expected_result == parsed_result


def test_count_valids():
    input_1 = InputLine(1, 3, "a", "abcde")
    input_2 = InputLine(1, 3, "b", "cdefg")
    input_3 = InputLine(2, 9, "c", "ccccccccc")

    assert 2 == count_valid([input_1, input_2, input_3])


def test_single_check_password_version2():
    low, high = (1, 3)
    letter = "a"
    password = "abcde"

    assert is_password_valid_v2(low, high, letter, password)
    assert not is_password_valid_v2(1, 3, "b", "bdbfg")


def test_count_valids_v2():
    input_1 = InputLine(1, 3, "a", "abcde")
    input_2 = InputLine(1, 3, "b", "cdefg")
    input_3 = InputLine(2, 9, "c", "ccccccccc")

    assert 1 == count_valid([input_1, input_2, input_3], checker=is_password_valid_v2)
