from typing import Dict


def grammar_to_regexp(grammar: str) -> str:
    rule_dict = build_rule_dict(grammar)

    return process_rule(0, rule_dict)


def process_rule(rule_idx: int, rule_dict: Dict[int, str]) -> str:
    rule = rule_dict[rule_idx]
    if rule[0] == '"' and rule[-1] == '"':
        return rule_dict[rule_idx][1:-1]
    elif '|' not in rule:
        return "".join(process_rule(int(sub_rule), rule_dict) for sub_rule in rule.split())
    else:
        sub_rules = rule.split('|')
        res = ""
        for sub_rule in sub_rules:
            res += "".join(process_rule(int(sub_sub_rule), rule_dict) for sub_sub_rule in sub_rule.split()) + "|"
        return res[:-1]



def build_rule_dict(grammar):
    rules = grammar.splitlines()
    rule_dict = {}
    for rule in rules:
        head, tail = rule.split(':')
        rule_number = int(head)
        tail = tail.strip()
        rule_dict[rule_number] = tail
    return rule_dict
