mandatory_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_present(passport: dict) -> bool:
    return all(key in passport for key in mandatory_keys)


def is_valid_year(entry: str, low: int, high: int) -> bool:
    return len(entry) == 4 and low <= int(entry) <= high


def is_byr_valid(entry: str) -> bool:
    return is_valid_year(entry, 1920, 2002)


def is_iyr_valid(entry: str) -> bool:
    return is_valid_year(entry, 2010, 2020)


def is_eyr_valid(entry: str) -> bool:
    return is_valid_year(entry, 2020, 2030)


def is_hgt_valid(entry: str) -> bool:
    try:
        unit = entry[-2:]
        if unit == "cm":
            return 150 <= int(entry[:-2]) <= 193
        elif unit == "in":
            return 59 <= int(entry[:-2]) <= 76
    except IndexError:
        pass
    return False


def is_hcl_valid(entry: str) -> bool:
    return len(entry) > 1 and entry[0] == "#" and is_hex_number_string(entry[1:])


def is_hex_number_string(entry: str) -> bool:
    try:
        int(entry, base=16)
    except ValueError:
        return False
    return True


def is_ecl_valid(entry: str) -> bool:
    return entry in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def is_pid_valid(entry: str) -> bool:
    return len(entry) == 9 and entry.isnumeric()


validations = {
    "byr": is_byr_valid,
    "iyr": is_iyr_valid,
    "eyr": is_eyr_valid,
    "hgt": is_hgt_valid,
    "hcl": is_hcl_valid,
    "ecl": is_ecl_valid,
    "pid": is_pid_valid,
    "cid": lambda _: True,
}


def is_valid_passport(passport: dict) -> bool:
    return is_present(passport) and all(
        validations[key](value) for key, value in passport.items()
    )
