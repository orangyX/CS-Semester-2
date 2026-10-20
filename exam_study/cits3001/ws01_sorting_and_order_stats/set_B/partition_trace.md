# 1. Trace partition(xs, 0, 7) on xs = [4, 8, 1, 6, 3, 7, 5]. Show the list after every swap, the value of mid, and the returned index.
The following table is given
| i | xs[i] | $\leq 5%?$ | swap | list | mid |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 4 | ✓ | $0 \leftrightarrow 0$ | ```[4, 8, 1, 6, 3, 7, 5]``` | 1 |
| 1 | 8 | ✗ | | ```[4, 8, 1, 6, 3, 7, 5]``` | 1 |
| 2 | 1 | ✓ | $1 \leftrightarrow 2$ | ```[4, 1, 8, 6, 3, 7, 5]``` | 2 |
| 3 | 8 | ✗ | | ```[4, 1, 8, 6, 3, 7, 5]``` | 2 |
| 4 | 3 | ✓ | $2 \leftrightarrow 4$ | ```[4, 1, 3, 6, 8, 7, 5]``` | 3 |
| 5 | 7 | ✗ | | ```[4, 1, 3, 6, 8, 7, 5]``` | 3 |
| 6 | 5 | ✓ | $3 \leftrightarrow 6$ | ```[4, 1, 3, 5, 8, 7, 6]``` | |

Then, for the full sort, calls are made about $[0, 7)$, $[2, 3)$, $[4, 4)$, $[5, 6)$, $[7, 7)$.