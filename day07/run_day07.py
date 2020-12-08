from helpers import get_data
from day07.bag_graph import BagGraph
from day07.bag_parsing import parse_input


def main():
    data = get_data(day=7)

    rules = parse_input(data)
    bag_graph = BagGraph(rules)

    my_bag = "shiny gold"

    my_bag_count = bag_graph.count_containing_bags(my_bag)

    print(f"There are {my_bag_count} bags that could contain a {my_bag} bag.")

    my_bag_contained = bag_graph.count_contained_bags(my_bag)
    print(f"And our single {my_bag} bag contains {my_bag_contained} other bags!")


if __name__ == "__main__":
    main()
