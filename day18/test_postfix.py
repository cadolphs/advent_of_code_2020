from infixpostfix import evaluate_postfix, infix_to_postfix
import pytest


@pytest.mark.parametrize("test_input, expected", [("2 3+", 5),
                                                  ("2 3 + 6 *", 30)])
def test_evaluate_postfix(test_input, expected):
    assert expected == evaluate_postfix(test_input)



@pytest.mark.parametrize("test_input, expected", [("2 * 3 + (4 * 5)", 26),
                                                  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
                                                  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
                                                  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),])
def test_postfix_conversion(test_input, expected):
    assert expected == evaluate_postfix(infix_to_postfix(test_input))


def test_conversion():
    assert infix_to_postfix("5 + (3 * 4)") == "5 3 4 *+"


@pytest.mark.parametrize("test_input, expected", [("2 * 3 + (4 * 5)", 46),
                                                  ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
                                                  ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
                                                  ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),])
def test_postfix_conversion_with_precedence(test_input, expected):
    precedences = {"+": 2, "*": 1}
    assert expected == evaluate_postfix(infix_to_postfix(test_input, precedences=precedences))