from helpers import get_data
from day04.parsing import parse_passports, to_password_dicts
from day04.passport_validation import is_valid


def main():
    data = get_data(day=4)
    passports = to_password_dicts(parse_passports(data))

    num_valid = sum(1 for passport in passports if is_valid(passport))

    print(f"There are {num_valid} valid passports.")


if __name__ == "__main__":
    main()
