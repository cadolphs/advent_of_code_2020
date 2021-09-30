from tile_handling import Tile
from tile_assembly import build_tile_fit_graph


def test_graph_simple():
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

    graph = build_tile_fit_graph([tile1, tile2])

    assert len(list(graph.edges())) == 1
    assert graph.has_edge((tile1, 1), (tile2, 3))
