import itertools


def get_checksum(values):
    return max(values) - min(values)


def get_result_of_even_division(values):
    values = sorted(values)

    all_combinations = itertools.product(values, repeat=2)
    for pair in all_combinations:
        # no check for zero division, because numbers are only positive
        division = pair[1] / pair[0]

        if division == int(division) and division != 1:
            return int(division)

    raise RuntimeError("No even division possible")


def get_sum(lines, function=None):
    if function is None:
        return 0

    total = 0
    for line in lines:
        values = [int(num) for num in line.split('\t')]

        try:
            total += function(values)
        except RuntimeError:
            pass

    return total


with open('data.txt', 'r') as f:
    lines = f.readlines()

print(get_sum(lines, get_checksum))
print(get_sum(lines, get_result_of_even_division))
