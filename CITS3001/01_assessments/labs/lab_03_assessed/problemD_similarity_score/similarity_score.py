import sys

def similarity_score(strA: str, strB: str) -> int:
    dpt = [[0 for _ in range(len(strB) + 1)] for _ in range(len(strA) + 1)]

    # In case_1.txt:
        # Columns -> strB
        # Rows -> strA
    for i in range(1, len(dpt)):
        for j in range(1, len(dpt[i])):
            # Engineer two cases:
                # Case 1: characters do not match -> take the maximum of two values; i-1 (above), and j-1 (left)
                # Case 2: characters match -> take the top left value from the current cell += 1
            if strA[i-1] != strB[j-1]:
                dpt[i][j] = max(dpt[i-1][j], dpt[i][j-1])
            elif strA[i-1] == strB[j-1]:
                dpt[i][j] = dpt[i-1][j-1] + 1

    return dpt[-1][-1]

inputs = sys.stdin.read().splitlines()
strA = inputs[0]
strB = inputs[1]

print(similarity_score(strA, strB))