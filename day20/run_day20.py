from helpers import get_data
from tile_handling import Tile, parse_input
from tile_assembly import build_tile_fit_graph, find_corner_tiles
import math

def main():
    tiles = parse_input(get_data(day=20))
    graph = build_tile_fit_graph(tiles)

    corner_tiles = find_corner_tiles(tiles, graph)

    print(f"The product of the four corner tiles is {math.prod(corner_tile.id for corner_tile in corner_tiles)}")


if __name__ == "__main__":
    main()