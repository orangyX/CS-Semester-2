#!/usr/bin/env python3
import sys


def reject(message):
    print(message, file=sys.stderr)
    sys.exit(1)

def parse_integers(line):
    # Remove preceeding '0' from lines, problemtool recommendation
    tokens = line.split()
    for token in tokens:
        if len(token) > 1 and token.startswith(b"0"):
            reject("Integers must not have leading zeros.")
    try:
        return list(map(int, tokens))
    except ValueError:
        reject("Input must contain integers in the specified format.")

lines = sys.stdin.buffer.read().splitlines()

# Minimum required lines (independent or no dependancies)
if len(lines) < 2:
    reject("Input requires n, m and times")


try:
    # Check first line for 2 integers 
    first_line = parse_integers(lines[0])
    if len(first_line) != 2:
        reject("First line must contain N and M.")
    n, m = first_line

    # Check domain and valid integers
    if not 1 <= n <= 100000:
        reject("N is outside the allowed range.")
    if n < 0:
        reject("N cannot be negative.")
    if not 0 <= m <= 100000:
        reject("M is outside the allowed range.")
    if m < 0:
        reject("M cannot be negative.")

    # The length of times must be the same as n 
    durations = parse_integers(lines[1])
    if len(durations) != n:
        reject("Must have a time for n tasks")
    if any(duration < 1 for duration in durations):
        reject("Task durations must be positive.")
    if len(lines) != m + 2:
        reject("There must be M relations")

    # Chekc format for remaining lines
    outgoing = [[] for _ in range(n)]
    in_degree = [0] * n

    for line in lines[2:]:
        relation = parse_integers(line)
        if len(relation) != 2:
            reject("Each dependency line must contain two tasks")
        previous, following = relation
        if not (1 <= previous <= n and 1 <= following <= n):
            reject("Relations must map to a node: 1 < N ")

        previous -= 1
        following -= 1
        outgoing[previous].append(following)
        in_degree[following] += 1

except ValueError:
    reject("Input must contain integers in the specified format.")

# Kahn's algorithm checks its acyclic.
queue = [task for task in range(n) if in_degree[task] == 0]
next_index = 0
visited = 0

while next_index < len(queue):
    task = queue[next_index]
    next_index += 1
    visited += 1

    for following in outgoing[task]:
        in_degree[following] -= 1
        if in_degree[following] == 0:
            queue.append(following)

if visited != n:
    reject("Dependencies must form a DAG.")

sys.exit(42)