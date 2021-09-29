import operator
import re


def infix_to_postfix(expr: str, precedences=None) -> str:
    if precedences == None:
        precedences = {'+': 1, '*': 1}

    tokens = re.findall(r"\(|\)|\+|\*|\d+", expr)
    new_expr = ""

    stack = []

    for token in tokens:
        if token.isnumeric():
            new_expr += token + ' '
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != "(":
                new_expr += stack.pop()
            if stack:
                assert stack[-1] == "("
                stack.pop()
        elif token in "+*":
            if not stack or stack[-1] == '(' or precedences[token] > precedences[stack[-1]]:
                stack.append(token)
            else:
                while stack and stack[-1] != "(" and precedences[token] <= precedences[stack[-1]]:
                    new_expr += stack.pop()
                stack.append(token)

    while stack:
        new_expr += stack.pop()

    return new_expr


def evaluate_postfix(expr: str) -> int:
    tokens = re.findall(r"\+|\*|\d+", expr)
    ops = {'+': operator.add, '*': operator.mul}

    stack = []
    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            func = ops[token]
            op1, op2 = stack.pop(), stack.pop()
            stack.append(func(op1, op2))

    return stack.pop()


def evaluate_infix(expr: str, precedences=None) -> int:
    return evaluate_postfix(infix_to_postfix(expr, precedences))