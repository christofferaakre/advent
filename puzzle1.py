def solve_part_1(puzzle_input: str):
    return sum(map(int, puzzle_input.splitlines()))


def solve_part_2(puzzle_input: str):
    unique_frequencies = set([0])
    frequency = 0

    while True:
        for increment in map(int, puzzle_input.split('\n')):
            frequency += increment

            if frequency in unique_frequencies:
                return frequency

            unique_frequencies.add(frequency)
