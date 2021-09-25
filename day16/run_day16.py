from helpers import get_data
from input_parser import read_input
from ticket_validation import find_all_invalid_numbers, drop_invalid_tickets


def main():
    rules, my_ticket, nearby_tickets = read_input(get_data(16))

    print("Sum of all invalid ticket numbers:", sum(find_all_invalid_numbers(nearby_tickets, rules)))

    valid_tickets = drop_invalid_tickets(nearby_tickets, rules)



if __name__ == "__main__":
    main()