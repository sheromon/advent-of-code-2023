

def parse_input(input_path):
    """Return lists of historical data."""
    data = []
    with open(input_path) as file_obj:
        for line in file_obj:
            data.append([int(val) for val in line.strip().split()])
    return data


def day09p1(input_file):
    """Return the sum of the next predicted values for each series."""
    history = parse_input(input_file)
    vals = []
    for row in history:
        deltas = [1]
        rows = [row]
        ind = 0
        while any(deltas):
            deltas = [rows[ind][a + 1] - rows[ind][a] for a in range(len(rows[ind]) - 1)]
            rows.append(deltas)
            ind += 1
        next_val = rows[-1][-1]
        while len(rows) > 1:
            row = rows.pop()
            next_val += rows[-1][-1]
        vals.append(next_val)
    return sum(vals)


def test09p1():
    assert 114 == day09p1('test_input.txt')


def day09p2(input_file):
    """Return the sum of the previous predicted values for each series."""
    history = parse_input(input_file)
    vals = []
    for row in history:
        deltas = [1]
        rows = [row]
        ind = 0
        while any(deltas):
            deltas = [rows[ind][a + 1] - rows[ind][a] for a in range(len(rows[ind]) - 1)]
            rows.append(deltas)
            ind += 1
        prev_val = rows[-1][0]
        while len(rows) > 1:
            row = rows.pop()
            prev_val -= rows[-1][0]
            prev_val *= -1
        vals.append(prev_val)
    return sum(vals)


def test09p2():
    assert 2 == day09p2('test_input.txt')


if __name__ == '__main__':
    test09p1()
    print('Day 09p1:', day09p1('day09_input.txt'))
    test09p2()
    print('Day 09p2:', day09p2('day09_input.txt'))
