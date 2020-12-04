from helpers import get_data
from day04.parsing import parse_passports, to_password_dicts
from day04.passport_validation import is_present, is_valid_passport


def main():
    data = get_data(day=4)
    passports = to_password_dicts(parse_passports(data))

    num_present = sum(1 for passport in passports if is_present(passport))

    print(f"There are {num_present} passports with all fields present.")

    num_valid = sum(1 for passport in passports if is_valid_passport(passport))

    print(f"There are {num_valid} valid passports")


if __name__ == "__main__":
    main()
