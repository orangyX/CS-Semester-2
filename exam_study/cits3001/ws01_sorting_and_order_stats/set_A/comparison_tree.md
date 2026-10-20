# 1. About the comparison tree
## 1.1. $N$ elements $\rightarrow$ $N!$ leaves, why?
* Each $N!$ input orderings requires a different permutation in order to sort it
* Two orderings reaching the same leaf would mean that the algorithm would apply the same rearrangement to both, getting at least one of these rearrangements incorrect
    * $\therefore$ there must be at least $N!$ possible arrangements
* Decision tree height: measures the maximum number of comparisons required (this is the worst case)

# 2. Find the fewest comparisons that any comparison sort must make in the worst case for $N=4$, $N=5$
Binary tree of height $h$ has at most $2^h$ leaves, thus $h \geq lgN!$

For $N=4$: consider $N! = 24$ possible permutations:
* For $h=4$, thus $2^h = 16$; thus $16 \ngeq 24$, insufficient.
* For $h=5$, $2^h=32$, hence $32 \geq 24$ as required.

$\therefore$ least $lg(24)=5$ comparisons are required, in the worst case.

Also consider for $N=5$, then $N!=32$ possible permutations:
* Let $h=7$, hence $2^h \geq N! \Longrightarrow 128 \geq 120$ as required.

$\therefore$ at least $lg(128)=7$ comparisons are required in the worst case.

# 3. Worst-case Find the worst-case comparison counts of insertion sort and merge sort (lecture code) for $N=4$, $N=5$

Insertion sort has $1 + 2 + 3 + ... + (N-1) = \frac{N(N-1)}{2}$ comparisons required in the worst-case.

For insertion sort:
* For $N=4$, then $\frac{4(4-1)}{2} = 6$ comparisons
* For $N=5$, then $\frac{5(5-1)}{2} = 10$ comparisons

Merge-sort has ${W(N) = W(\lfloor \frac{N}{2} \rfloor)} + W(\lceil \frac{N}{2} \rceil) + (N-1)$

For merge-sort:
| $N$ | Split | $W(N)$ |
| :--- | :--- | :--- |
| 1 | None | 0 |
| 2 | $1 \mid 1$ | $0+0+1$ |
| 3 | $1 \mid 2$ | $0+1+2$ |
| 4 | $2 \mid 2$ | $1+1+3$ |
| 5 | $2 \mid 3$ | $1+3+4$ |

$\therefore$ for $N=5$, there can be at most $8$ comparisons.

# 4. $N=5$ exceeds your answer to (b). Does that contradict "merge sort is optimal"?
Merge-sort is optimal (i.e., it runs in the fastest-possible time to solve the problem (sorting in $O(NlgN)$ time in its worst-case)).
* Comparison-based sorting algorithm performance is bounded below by $\Theta(NlgN)$, and bounded above by $\Omega(NlgN)$.
* Asymptotic complexity measures the overall running time of an algorithm ignoring contant factors and small $N$, as above.