from ticket_validation import is_ticket_completely_invalid, find_all_invalid_numbers, drop_invalid_tickets, rule_to_column_algo
from pytest import fixture
from input_parser import read_input
import numpy as np

@fixture
def sample_inputs():
    sample_input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    return read_input(sample_input)


@fixture
def valid_ticket_input():
    sample_input = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
    return read_input(sample_input)


def test_recognizes_a_completely_invalid_ticket(sample_inputs):
    rules, _, _ = sample_inputs

    assert is_ticket_completely_invalid([40, 4, 50], rules)
    assert not is_ticket_completely_invalid([7, 3, 47], rules)


def test_finds_invalid_numbers(sample_inputs):
    rules, _, nearby_tickets = sample_inputs

    assert list(find_all_invalid_numbers(nearby_tickets, rules)) == [4, 55, 12]

    just_valid = drop_invalid_tickets(nearby_tickets, rules)

    assert len(just_valid) == 1
    assert just_valid[0] == [7, 3, 47]


def test_algo(valid_ticket_input):
    rules, _, nearby_tickets = valid_ticket_input

    mat = np.array(nearby_tickets)

    res = rule_to_column_algo(mat, rules)

    print(res)
    assert False