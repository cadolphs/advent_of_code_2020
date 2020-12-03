def positions(start, direction, max_row):
    current = start
    while current[1] < max_row:
        yield current
        current = (current[0] + direction[0], current[1] + direction[1])
