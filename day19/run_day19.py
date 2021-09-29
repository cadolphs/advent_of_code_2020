import re

from helpers import get_data
from regexp_builder import grammar_to_regexp


def main():
    input_str = get_data(day=19)
    grammar, messages = read_data(input_str)
    regexp = grammar_to_regexp(grammar)
    pattern = re.compile(regexp)

    num_match = sum(check_message(pattern, message) for message in messages)

    print(f"There's {num_match} messages matching the rule.")


def check_message(pattern, message):
    return pattern.match(message) is not None


def read_data(input_str):
    blocks = input_str.split('\n\n')
    return blocks[0], blocks[1].splitlines()


if __name__ == "__main__":
    main()