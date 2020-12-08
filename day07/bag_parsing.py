from typing import List, NamedTuple
import pyparsing as pp


def combine_colors(tokens: pp.ParseResults) -> str:
    return f"{tokens[0]} {tokens[1]}"


color = pp.Group(pp.Word(pp.alphas) * 2)
number = pp.Word(pp.nums)
bags_cont = pp.Suppress("bags contain")
bag_or_bags = pp.Suppress(pp.Literal("bag") ^ pp.Literal("bags"))

empty_line = pp.Group(
    color + pp.Suppress("bags contain no other bags.")
).setResultsName("empty")

inner_bag_token = pp.Group(number + color + bag_or_bags + pp.Suppress(pp.oneOf(". ,")))


class ContainedBag(NamedTuple):
    num: int
    color: str


# Rule = namedtuple("Rule", ["color", "contained_bags"])
class Rule(NamedTuple):
    color: str
    contained_bags: List[ContainedBag]


multi_line = pp.Group(
    color + bags_cont + pp.Group(inner_bag_token[1, ...])
).setResultsName("multi")

line = empty_line | multi_line


def process_multi(parse_result: pp.ParseResults) -> Rule:
    color = combine_colors(parse_result[0])
    inner_bags = parse_result[1]

    inner_bags_lst = []
    for bag in inner_bags:
        num = int(bag[0])
        inner_color = combine_colors(bag[1])
        inner_bags_lst.append(ContainedBag(num, inner_color))

    return Rule(color, inner_bags_lst)


def parse_rule(rule: str) -> Rule:
    parse_result = line.parseString(rule)

    if "empty" in parse_result:
        return process_empty_bag(parse_result["empty"])
    elif "multi" in parse_result:
        return process_multi(parse_result["multi"])


def process_empty_bag(parse_result: pp.ParseResults) -> Rule:
    color = combine_colors(parse_result[0])

    return Rule(color=color, contained_bags=[])


def parse_input(data: str) -> List[Rule]:
    return [parse_rule(line) for line in data.split("\n")]
