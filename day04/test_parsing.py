from day04.parsing import parse_entry, parse_passports, to_password_dicts


def test_parse_single_entry():
    text = "ecl:gry"

    parsed = parse_entry(text)

    expected = ("ecl", "gry")

    assert expected == parsed

    assert expected == parsed


def test_parse_blank_lines_separately():
    text = "ecl:gry pid:8600\nfoo:baz\n\neyr:2020 hcl:#fffffd"

    parsed = parse_passports(text)

    expected = [
        [["ecl", "gry"], ["pid", "8600"], ["foo", "baz"]],
        [["eyr", "2020"], ["hcl", "#fffffd"]],
    ]

    assert expected == parsed


def test_to_password_dicts():
    text = "ecl:gry pid:8600\nfoo:baz\n\neyr:2020 hcl:#fffffd"

    parsed = parse_passports(text)

    dicts = to_password_dicts(parsed)

    expected_0 = {"ecl": "gry", "pid": "8600", "foo": "baz"}
    expected_1 = {"eyr": "2020", "hcl": "#fffffd"}

    assert [expected_0, expected_1] == dicts
