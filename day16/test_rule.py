from rule import Rule
from input_parser import parse_rule_line, read_input

def test_a_bit_of_containment():
    my_rule = Rule("some rule", (1, 42), (55,99))

    assert my_rule.is_valid(1)
    assert my_rule.is_valid(42)
    assert not my_rule.is_valid(0)
    assert not my_rule.is_valid(43)
    assert my_rule.is_valid(55)
    assert my_rule.is_valid(99)
    assert my_rule.is_valid(35)
    assert my_rule.is_valid(60)
    assert not my_rule.is_valid(54)
    assert not my_rule.is_valid(100)

def test_rule_parsing():
    line = "departure gate: 1-42 or 55-104"
    rule = parse_rule_line(line)

    assert rule.name == "departure gate"
    assert rule.range1 == (1, 42)
    assert rule.range2 == (55, 104)

def test_overall_parsing():
    test_input = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

    rules, my_ticket, nearby_tickets = read_input(test_input)

    assert len(rules) == 3
    assert rules[0].name == "class"
    # don't need to check if overall rule parsing worked because we have a test for that

    assert my_ticket == [11, 12, 13]
    assert nearby_tickets == [[3, 9, 18], [15, 1, 5], [5, 14, 9]]