import pytest

from helpers import get_data
from tile_handling import Tile, parse_input
from tile_assembly import build_tile_fit_graph, find_corner_tiles

tile1 = ("Tile 1951:\n"
         "#.##...##.\n"
         "#.####...#\n"
         ".....#..##\n"
         "#...######\n"
         ".##.#....#\n"
         ".###.#####\n"
         "###.##.##.\n"
         ".###....#.\n"
         "..#.#..#.#\n"
         "#...##.#..")
tile2 = ("Tile 2311:\n"
         "..##.#..#.\n"
         "##..#.....\n"
         "#...##..#.\n"
         "####.#...#\n"
         "##.##.###.\n"
         "##...#.###\n"
         ".#.#.#..##\n"
         "..#....#..\n"
         "###...#.#.\n"
         "..###..###")

tile1 = Tile.from_str(tile1)
tile2 = Tile.from_str(tile2)


@pytest.fixture
def example_input():
    input_str = ("Tile 2311:\n"
                 "..##.#..#.\n"
                 "##..#.....\n"
                 "#...##..#.\n"
                 "####.#...#\n"
                 "##.##.###.\n"
                 "##...#.###\n"
                 ".#.#.#..##\n"
                 "..#....#..\n"
                 "###...#.#.\n"
                 "..###..###\n"
                 "\n"
                 "Tile 1951:\n"
                 "#.##...##.\n"
                 "#.####...#\n"
                 ".....#..##\n"
                 "#...######\n"
                 ".##.#....#\n"
                 ".###.#####\n"
                 "###.##.##.\n"
                 ".###....#.\n"
                 "..#.#..#.#\n"
                 "#...##.#..\n"
                 "\n"
                 "Tile 1171:\n"
                 "####...##.\n"
                 "#..##.#..#\n"
                 "##.#..#.#.\n"
                 ".###.####.\n"
                 "..###.####\n"
                 ".##....##.\n"
                 ".#...####.\n"
                 "#.##.####.\n"
                 "####..#...\n"
                 ".....##...\n"
                 "\n"
                 "Tile 1427:\n"
                 "###.##.#..\n"
                 ".#..#.##..\n"
                 ".#.##.#..#\n"
                 "#.#.#.##.#\n"
                 "....#...##\n"
                 "...##..##.\n"
                 "...#.#####\n"
                 ".#.####.#.\n"
                 "..#..###.#\n"
                 "..##.#..#.\n"
                 "\n"
                 "Tile 1489:\n"
                 "##.#.#....\n"
                 "..##...#..\n"
                 ".##..##...\n"
                 "..#...#...\n"
                 "#####...#.\n"
                 "#..#.#.#.#\n"
                 "...#.#.#..\n"
                 "##.#...##.\n"
                 "..##.##.##\n"
                 "###.##.#..\n"
                 "\n"
                 "Tile 2473:\n"
                 "#....####.\n"
                 "#..#.##...\n"
                 "#.##..#...\n"
                 "######.#.#\n"
                 ".#...#.#.#\n"
                 ".#########\n"
                 ".###.#..#.\n"
                 "########.#\n"
                 "##...##.#.\n"
                 "..###.#.#.\n"
                 "\n"
                 "Tile 2971:\n"
                 "..#.#....#\n"
                 "#...###...\n"
                 "#.#.###...\n"
                 "##.##..#..\n"
                 ".#####..##\n"
                 ".#..####.#\n"
                 "#..#.#..#.\n"
                 "..####.###\n"
                 "..#.#.###.\n"
                 "...#.#.#.#\n"
                 "\n"
                 "Tile 2729:\n"
                 "...#.#.#.#\n"
                 "####.#....\n"
                 "..#.#.....\n"
                 "....#..#.#\n"
                 ".##..##.#.\n"
                 ".#.####...\n"
                 "####.#.#..\n"
                 "##.####...\n"
                 "##..#.##..\n"
                 "#.##...##.\n"
                 "\n"
                 "Tile 3079:\n"
                 "#.#.#####.\n"
                 ".#..######\n"
                 "..#.......\n"
                 "######....\n"
                 "####.#..#.\n"
                 ".#...#.##.\n"
                 "#.#####.##\n"
                 "..#.###...\n"
                 "..#.......\n"
                 "..#.###...")
    return parse_input(input_str)


def test_graph_simple():
    graph = build_tile_fit_graph([tile1, tile2])

    assert len(list(graph.edges())) == 2
    assert graph.has_edge((tile1, 1, 1), (tile2, 3, 1))
    assert graph.has_edge((tile1, 1, -1), (tile2, 3, -1))


@pytest.mark.skip
def test_playground():
    all_tiles = parse_input(get_data(day=20))
    graph = build_tile_fit_graph(all_tiles)

    print(max(graph.degree(node) for node in graph.nodes()))
    print(min(graph.degree(node) for node in graph.nodes()))

    assert len(find_corner_tiles(all_tiles, graph)) == 4
