import sys

def lcs(x: str, y: str) -> int:
    prev = [0] * (len(x) + 1)
    curr = [0] * (len(y) + 1)

    for j in range(0, len(y)):
        for i in range(0, len(x) + 1):
            if x[i-1] == y[j]:
                curr[i] = prev[i-1] + 1
            else:
                curr[i] = max(curr[i-1], prev[i])

        prev, curr = curr, prev

    return prev[-1]

inputs = sys.stdin.read().split()
x, y = inputs[0], inputs[1]

print(lcs(x, y))