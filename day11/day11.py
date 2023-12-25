

def parse_input(input_path):
    """Return coordinates of galaxies."""
    coords = []
    row = 0
    with open(input_path) as file_obj:
        for line in file_obj:
            if row == 0:
                n_cols = len(line.strip())
            for col, char in enumerate(line.strip()):
                if char == '#':
                    coords.append((row, col))
            row += 1
    n_rows = row
    return coords, n_rows, n_cols


def expand(coords, n_rows, n_cols, expansion_factor=2):
    """Expand the space between the galaxies based on the expansion factor."""
    row_inds, col_inds = zip(*coords)
    row_map = {row: row for row in set(row_inds)}
    delta = 0
    for row in range(n_rows):
        if row not in row_map:
            delta += (expansion_factor - 1)
        row_map[row] = row + delta

    col_map = {col: col for col in set(col_inds)}
    delta = 0
    for col in range(n_cols):
        if col not in col_map:
            delta += (expansion_factor - 1)
        col_map[col] = col + delta

    return [(row_map[row], col_map[col]) for row, col in coords]


def calc_distance(coords1, coords2):
    """Return the shortest distance between a pair of galaxies."""
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


def day11(input_file, expansion_factor=2):
    """Return the sum of the shortest distance between each pair of galaxies."""
    coords, n_rows, n_cols = parse_input(input_file)
    new_coords = expand(coords, n_rows, n_cols, expansion_factor)

    total_dist = 0
    for ind1 in range(len(new_coords)):
        for ind2 in range(ind1 + 1, len(new_coords)):
            total_dist += calc_distance(new_coords[ind1], new_coords[ind2])
    return total_dist


def test11p1():
    coords, n_rows, n_cols = parse_input('test_input.txt')
    new_coords = expand(coords, n_rows, n_cols)
    assert 9 == calc_distance(new_coords[4], new_coords[8])
    assert 15 == calc_distance(new_coords[0], new_coords[6])
    assert 17 == calc_distance(new_coords[2], new_coords[5])
    assert 5 == calc_distance(new_coords[7], new_coords[8])

    assert 374 == day11('test_input.txt')


def test11p2():
    assert 1030 == day11('test_input.txt', expansion_factor=10)
    assert 8410 == day11('test_input.txt', expansion_factor=100)


if __name__ == '__main__':
    test11p1()
    print('Day 11p1:', day11('day11_input.txt'))
    test11p2()
    print('Day 11p2:', day11('day11_input.txt', expansion_factor=1000000))
