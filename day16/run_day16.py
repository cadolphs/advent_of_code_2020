from helpers import get_data
from input_parser import read_input
from ticket_validation import find_all_invalid_numbers, drop_invalid_tickets, rule_to_column_algo, specific_puzzle_question
import numpy as np

def main():
    rules, my_ticket, nearby_tickets = read_input(get_data(16))

    print("Sum of all invalid ticket numbers:", sum(find_all_invalid_numbers(nearby_tickets, rules)))

    valid_tickets = drop_invalid_tickets(nearby_tickets, rules)

    mat = np.array(valid_tickets)
    rules_ticket_correspondence = rule_to_column_algo(mat, rules)
    specific_answer = specific_puzzle_question(my_ticket, rules_ticket_correspondence)

    print(f"Product of your ticket's departure numbers is {specific_answer}")


if __name__ == "__main__":
    main()