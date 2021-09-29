from regexp_builder import grammar_to_regexp
from hypothesis import given
import hypothesis.strategies as some

@given(some.characters(whitelist_categories='L'))
def test_single_character_becomes_single_character(c):
    test_input = f'0: "{c}"'
    expected = c

    assert expected == grammar_to_regexp(test_input)


def test_a_single_rule_is_just_followed():
    test_input = '''0: 1
1: "c"'''

    expected = "c"

    assert expected == grammar_to_regexp(test_input)


def test_two_rules_are_correctly_expanded():
    test_input = '''0: 1 2
1: "a"
2: "f"'''

    expected = "af"
    assert expected == grammar_to_regexp(test_input)


def test_down_the_rabbithole():
    test_input = '''0: 1 2
1: 3
2: 4
3: "c"
4: "u"'''

    expected = "cu"
    assert expected == grammar_to_regexp(test_input)


def test_one_rule_or():
    test_input = '''0: 1 | 2
1: "x"
2: "y"'''

    expected = 'x|y'
    assert expected == grammar_to_regexp(test_input)


def test_two_rule_or():
    test_input = '''0: 1 2 | 3 4
1: "a"
2: "b"
3: "x"
4: "y"'''

    expected = 'ab|xy'
    assert expected == grammar_to_regexp(test_input)