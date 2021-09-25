from rule import Rule
from typing import List, Iterable
from itertools import chain
import numpy as np

def is_ticket_completely_invalid(ticket: List[int], rules: List[Rule]) -> bool:
    return any(all(not rule.is_valid(number) for rule in rules) for number in ticket)


def drop_invalid_tickets(tickets: List[List[int]], rules: List[Rule]) -> List[List[int]]:
    return [ticket for ticket in tickets if not is_ticket_completely_invalid(ticket, rules)]


def find_completely_invalid_numbers(ticket: List[int], rules: List[Rule]) -> Iterable[int]:
    return (number for number in ticket if all(not rule.is_valid(number) for rule in rules))


def find_all_invalid_numbers(tickets: List[List[int]], rules: List[Rule]) -> List[int]:
    return chain.from_iterable(find_completely_invalid_numbers(ticket, rules) for ticket in tickets)


def find_columns_valid_for_rule(ticket_matrix, rule: Rule) -> List[int]:
    mask = rule.is_valid_vectorized(ticket_matrix)
    return np.nonzero(np.all(mask == 1, axis=0))