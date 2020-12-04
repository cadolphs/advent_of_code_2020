from day04.passport_validation import is_present


def test_valid_passport():
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    vals = [1, 2, 3, 4, 5, 6, 7, 8]

    test_pp = dict(zip(keys, vals))

    assert is_present(test_pp)


def test_invalid_passport():
    keys = ["byr", "iyr", "hgt", "hcl", "ecl", "pid", "cid"]
    vals = [1, 2, 3, 5, 6, 7, 8]

    test_pp = dict(zip(keys, vals))

    assert not is_present(test_pp)
