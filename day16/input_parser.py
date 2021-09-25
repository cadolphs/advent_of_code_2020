import re
from rule import Rule
from typing import List

rule_re = re.compile(r"(?P<name>.+): (?P<low1>\d+)-(?P<high1>\d+) or (?P<low2>\d+)-(?P<high2>\d+)")


def read_input(input_as_text: str):
    blocks = input_as_text.split('\n\n')

    rule_block = blocks[0].split('\n')
    rules = [parse_rule_line(rule_line) for rule_line in rule_block]

    my_ticket = parse_ticket_line(blocks[1].split('\n')[1])

    nearby_ticket_lines = blocks[2].split('\n')[1:]
    nearby_tickets = [parse_ticket_line(ticket_line) for ticket_line in nearby_ticket_lines]

    return rules, my_ticket, nearby_tickets


def parse_rule_line(rule_line: str) -> Rule:
    res = re.match(rule_re, rule_line)

    return Rule(name=res.group('name'),
                range1=(int(res.group('low1')), int(res.group('high1'))),
                range2=(int(res.group('low2')), int(res.group('high2'))),)


def parse_ticket_line(ticket_line: str) -> List[int]:
    return [int(number) for number in ticket_line.split(',')]