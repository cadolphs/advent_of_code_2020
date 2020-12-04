mandatory_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_valid(passport: dict) -> bool:
    return all(key in passport for key in mandatory_keys)
