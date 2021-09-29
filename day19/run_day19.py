import re

from helpers import get_data
from regexp_builder import grammar_to_regexp, build_rule_dict, process_rule


def main():
    input_str = get_data(day=19)
    grammar, messages = read_data(input_str)
    regexp = grammar_to_regexp(grammar)
    pattern = re.compile(regexp)

    num_match = sum(check_message(pattern, message) for message in messages)

    print(f"There's {num_match} messages matching the rule.")

    res = part2(grammar, messages)
    print(f"There's now {res} matching messages with the new rules.")

def check_message(pattern, message):
    return pattern.match(message) is not None


def read_data(input_str):
    blocks = input_str.split('\n\n')
    return blocks[0], blocks[1].splitlines()


def part2(grammar, messages):
    rule_dict = build_rule_dict(grammar)

    rule_dict[8] = "42 | 42 8" # Just so that it blows up when there's _actually_ any loops.
    rule_dict[11] = "42 31 | 42 11 31"

    pattern42 = process_rule(42, rule_dict)
    pattern31 = process_rule(31, rule_dict)

    new_re = f"^(?P<pattern42>({pattern42})+)(?P<pattern31>({pattern31})+)$"
    pattern = re.compile(new_re)

    count = 0
    for message in messages:
        match = pattern.match(message)
        if match:
            group42 = match.group("pattern42")
            group31 = match.group("pattern31")

            # This works but only because rules 42 and 31 have same string length. Otherwise we'd have to count
            # how often it actually matches.
            if len(group42) > len(group31):
                count += 1
    return count


if __name__ == "__main__":
    main()