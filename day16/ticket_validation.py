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


def find_all_invalid_numbers(tickets: List[List[int]], rules: List[Rule]) -> Iterable[int]:
    return chain.from_iterable(find_completely_invalid_numbers(ticket, rules) for ticket in tickets)


def build_ticket_rule_matrix(ticket_matrix, rules: List[Rule]) -> np.ndarray:
    # There's probably no fast way to make this happen, eh?

    num_columns = ticket_matrix.shape[1]
    ticket_rule_mat = np.zeros((num_columns, len(rules)))
    for i in range(num_columns):
        for j, rule in enumerate(rules):
            if np.alltrue(rule.is_valid_vectorized(ticket_matrix[:, i])):
                ticket_rule_mat[i, j] = 1

    return ticket_rule_mat


def rule_to_column_algo(ticket_matrix, rules: List[Rule]):

    ticket_rule_matrix = build_ticket_rule_matrix(ticket_matrix, rules)
    rule_ticket_correspondence = []

    while not np.all(ticket_rule_matrix == 0):
        # find either a row or a column with only 1s
        colum_sums = ticket_rule_matrix.sum(axis=0)
        ones_in_colum_sums = np.where(colum_sums == 1)[0]
        row_sums = ticket_rule_matrix.sum(axis=1)
        ones_in_row_sums = np.where(row_sums == 1)[0]

        if len(ones_in_colum_sums) > 0:
            col = ones_in_colum_sums[0]
            row = np.where(ticket_rule_matrix[:, col] == 1)[0][0]
        elif len(ones_in_row_sums) > 0:
            row = ones_in_row_sums[0]
            col = np.where(ticket_rule_matrix[row, :] == 1)[0][0]
        else:
            # No row or col with exactly one '1'. Either we're done or we're screwed
            if not np.all(ticket_rule_matrix == 0):
                raise NotImplementedError("Don't know yet how to do search and branching.")

        rule_ticket_correspondence.append((row, col))
        ticket_rule_matrix[row, :] = 0
        ticket_rule_matrix[:, col] = 0

        rule_ticket_correspondence.sort(key=lambda item: item[0])
    return [(col+1, rules[rule].name) for col, rule in rule_ticket_correspondence]

