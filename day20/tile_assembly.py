import math

from tile_handling import Tile
from typing import List
import networkx as nx
from itertools import combinations, product


def build_tile_fit_graph(tiles: List[Tile]) -> nx.Graph:
    """Create a graph where nodes are tuples of Tile and side and edges exist if the two tiles agree along those
    sides. """

    graph = nx.Graph()
    # First add all tiles, sides, and alignments as nodes so we know which ones don't match anything.
    for tile, side, alignment in product(tiles, range(4), [-1, 1]):
        graph.add_node((tile, side, alignment))

    for tile1, tile2 in combinations(tiles, 2):
        for side1, side2 in product([0, 1, 2, 3], repeat=2):
            for alignment in [-1, 1]:
                if tile1.matches(tile2, side=side1, other_side=side2, alignment=alignment):
                    graph.add_edge((tile1, side1, 1), (tile2, side2, alignment))
                    graph.add_edge((tile1, side1, -1), (tile2, side2, -alignment))

    return graph


def find_corner_tiles(tiles: List[Tile], graph: nx.Graph) -> List[Tile]:
    alignment = 1  # Doesn't matter, just pick one

    def num_neighbors(tile: Tile) -> int:
        return sum(graph.degree((tile, side, alignment)) for side in range(4))

    corner_tiles = [tile for tile in tiles if num_neighbors(tile) == 2]
    return corner_tiles
