from typing import Iterable, Optional
import networkx as nx
from networkx.algorithms.dag import descendants, ancestors
from day07.bag_parsing import Rule


class BagGraph:
    def __init__(self, rules: Optional[Iterable[Rule]] = None):
        self._graph = nx.DiGraph()
        if rules:
            self.add_rules(rules)

    def add_rule(self, rule: Rule):
        self._graph.add_node(rule.color)
        for contained_bag in rule.contained_bags:
            self._graph.add_edge(rule.color, contained_bag.color, num=contained_bag.num)

    def count_containing_bags(self, color: str) -> int:
        try:
            succs = ancestors(self._graph, color)
        except nx.NetworkXError:
            raise ValueError(f"No rule for {color} bags exists!")
        return sum(1 for succ in succs)

    def add_rules(self, rules: Iterable[Rule]):
        for rule in rules:
            self.add_rule(rule)

    def count_contained_bags(self, color: str) -> int:
        return sum(
            self._graph.get_edge_data(color, node)["num"]
            * (self.count_contained_bags(node) + 1)
            for node in self._graph.successors(color)
        )
