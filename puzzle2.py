def solve_part_1(puzzle_input: str):
    twos = 0
    threes = 0

    strings = puzzle_input.splitlines()
    for string in strings:
        singles = set()
        doubles = set()
        triples = set()
        passed = set()
        for character in string:
            if character in passed:
                continue
            if character in triples:
                triples.remove(character)
                passed.add(character)
            if character in doubles:
                triples.add(character)
                doubles.remove(character)
            elif character in singles:
                doubles.add(character)
                singles.remove(character)
            else:
                singles.add(character)
        if len(doubles) >= 1:
            twos += 1
        if len(triples) >= 1:
            threes += 1
    return twos * threes


def solve_part_2(puzzle_input: str):
    common_characters = ''
    strings = puzzle_input.splitlines()
    # Finding sibling strings
    for str1 in strings:
        for str2 in strings:
            mismatches = 0
            for i in range(0, len(str1) - 1):
                if str1[i] != str2[i]:
                    mismatches += 1
            if mismatches == 1:
                string1 = str1
                string2 = str2
    # Extracting common characters
    for i in range(0, len(string1)):
        if string1[i] == string2[i]:
            common_characters += string1[i]
    print(string1)
    print(string2)
    return common_characters
