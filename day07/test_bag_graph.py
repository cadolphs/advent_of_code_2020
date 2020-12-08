from pyparsing import ParserElement
from day07.bag_graph import BagGraph
from day07.bag_parsing import Rule, ContainedBag
from day07.bag_parsing import parse_input


def test_add_empty_rule():
    graph = BagGraph()
    test_rule = Rule("bright yellow", [])

    graph.add_rule(test_rule)

    assert graph.count_containing_bags("bright yellow") == 0


def test_add_single_rule():
    graph = BagGraph()
    test_rule = Rule("bright white", [ContainedBag(1, "shiny gold")])

    graph.add_rule(test_rule)

    assert graph.count_containing_bags("shiny gold") == 1


def test_example_input_part_1():
    test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

    rules = parse_input(test_input)

    bag_graph = BagGraph()
    bag_graph.add_rules(rules)

    assert 4 == bag_graph.count_containing_bags("shiny gold")


def test_counting_empty():
    graph = BagGraph()
    test_rule = Rule("bright yellow", [])

    graph.add_rule(test_rule)

    assert graph.count_contained_bags("bright yellow") == 0


def test_count_single_edge():
    test_rule = Rule("bright yellow", [ContainedBag(3, "purple vomit")])
    graph = BagGraph([test_rule])

    assert 3 == graph.count_contained_bags("bright yellow")


def test_count_multiple_edges_depth1():
    test_rule = Rule(
        "bright yellow",
        [ContainedBag(3, "purple vomit"), ContainedBag(5, "ocean blue")],
    )
    graph = BagGraph([test_rule])

    assert 8 == graph.count_contained_bags("bright yellow")


def test_count_multiple_edges_depth_2():
    rule_1 = Rule("bright yellow", [ContainedBag(2, "ocean blue")])
    rule_2 = Rule("ocean blue", [ContainedBag(3, "purple rain")])

    graph = BagGraph([rule_1, rule_2])

    # bright yellow bag contains 2 ocean blue bags, and then 2 * 3 purple rain bags = 8 total bags

    assert 8 == graph.count_contained_bags("bright yellow")


def test_on_example_input_part2():
    test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

    rules = parse_input(test_input)

    bag_graph = BagGraph()
    bag_graph.add_rules(rules)

    assert 32 == bag_graph.count_contained_bags("shiny gold")
