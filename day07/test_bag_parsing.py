from day07.bag_parsing import Rule, ContainedBag, parse_rule


def test_single_bag_rule():
    text = "bright white bags contain 1 shiny gold bag."

    rule = parse_rule(text)

    expected = Rule("bright white", [ContainedBag(1, "shiny gold")])

    assert expected == rule


def test_empty_bag_rule():
    text = "bright white bags contain no other bags."

    rule = parse_rule(text)

    expected = Rule("bright white", [])

    assert expected == rule


def test_multi_rule():
    text = "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."

    rule = parse_rule(text)

    expected = Rule(
        "muted yellow", [ContainedBag(2, "shiny gold"), ContainedBag(9, "faded blue")]
    )

    assert expected == rule