import math

from tile_handling import Tile
from typing import List
import networkx as nx
from itertools import combinations, product


def arrange_all_tiles(tiles: List[Tile]):
    graph = build_tile_fit_graph(tiles)

    new_pairings = nx.MultiGraph()

    # Find a pair of tiles that one of them only matches for exactly one. What does that mean? It means it
    # has exactly one neighbor.
    while graph:
        candidate = find_candidate(graph)
        neighbor = next(graph.neighbors(candidate))

        new_pairings.add_edge(candidate[0], neighbor[0], side1=candidate[1], side2=neighbor[1])

        # Skip the alignment for now; just remove them
        graph.remove_node(candidate)
        graph.remove_node(neighbor)

    # Pairings are now "by node" so we can assign them positions.
    dimension = len(tiles)
    n = int(math.sqrt(dimension))

    tile_positions = {}



    return True


def find_candidate(graph):
    candidates = (node for node in graph.nodes if graph.degree(node) == 1)
    return next(candidates)


def build_tile_fit_graph(tiles: List[Tile]) -> nx.Graph:
    """Create a graph where nodes are tuples of Tile and side and edges exist if the two tiles agree along those
    sides. """

    graph = nx.Graph()
    for tile1, tile2 in combinations(tiles, 2):
        for side1, side2 in product([0,1,2,3], repeat=2):
            if tile1.matches(tile2, side=side1, other_side=side2):
                graph.add_edge((tile1, side1), (tile2, side2))

    return graph
