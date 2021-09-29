from helpers import get_data
from infixpostfix import evaluate_infix


def main():
    expressions = get_data(day=18).splitlines()

    answer = sum(evaluate_infix(expression) for expression in expressions)

    print(f"Sum of all expressions evaluates to {answer}.")

    precedences = {"+": 2, "*": 1}

    answer = sum(evaluate_infix(expression, precedences=precedences) for expression in expressions)

    print(f"Sum of all expressions evaluates to {answer}.")

if __name__ == "__main__":
    main()
