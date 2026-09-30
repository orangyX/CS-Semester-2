import sys

"""
    The main purpose of this file is to ensure that all .in files are strictly formatted
"""

inputs = sys.stdin.read()

# Check if inputs are empty
if not inputs:
    exit(43)

# The file must end with \n
if inputs[-1] != '\n':
    exit(43)

try:
    assert('\r' not in inputs)
except AssertionError as e:
    exit(43)

inputs = inputs.split("\n")
inputs = inputs[:len(inputs) - 1] # Have to remove the '' at the end, otherwise valid files are rejected

def validate_format(ln: str) -> None:
    """
        Validation function; checks if entries in .in is of valid format:
            - Non-negative value
            - Digit values
            - Format-specific checks (such as double space, or \t which are rejected)
    """

    ln = ln.split(" ") # Split on a single space; anything with more than a single space is rejected (or on \t)

    try:
        assert(len(ln) == 3)

        for i in ln:
            assert(i.isdigit() and not (len(i) > 1 and i.startswith('0')))
    except AssertionError as e:
        exit(43)

def validate_bound(ln: str, num_vert: int) -> None:
    """
        Validation function; checks if entries in .in is of valid bounds/datatypes
            - Ensures that graph is connected (checks that u, v have a key < |V|)
    """
    ln = ln.split()

    u, v, _ = int(ln[0]), int(ln[1]), int(ln[2])

    try:
        assert(u < num_vert and v < num_vert)
    except AssertionError as e:
        exit(43)

num_vert = 0
num_edge = 0
num_line = 0

for i in range(len(inputs)):
    if i == 0:
        validate_format(inputs[i])
        num_vert = int(inputs[i].split()[0])
        num_edge = int(inputs[i].split()[1])

        try:
            assert(num_edge >= num_vert - 1) # A connected graph has at least V-1 edges; check that there are V-1 edges at least
        except AssertionError as e:
            exit(43)
    else:
        validate_format(inputs[i])
        validate_bound(inputs[i], num_vert)
        num_line += 1

try:
    assert(num_edge == num_line) # For |E| edges, then there must be |E| lines
except AssertionError as e:
    exit(43)

# Success; the input is valid
exit(42)