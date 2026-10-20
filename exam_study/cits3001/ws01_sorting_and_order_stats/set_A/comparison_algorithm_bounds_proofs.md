# 1. Prove that $O(lgN!) \subseteq O(NlgN)$
For $N$ factors of $N!=1 \cdot 2 \cdot 3 \cdot ... \cdot N$, then $N! \leq N^N$, therefore:
$$
N! \leq N^N\\
\equiv lgN! \leq lgN^N\\
\equiv lgN! \ NlgN
$$

Hence $lgN!$ is bounded above by $NlgN$, hence $O(lgN!)\supseteq O(NlgN)$.

# 2. Prove that $O(lgN!) \supseteq O(NlgN)$
Factorsof $N!$ are paired with those of $N!$, yielding:
$$
N!^2 = \prod_{k=1}^{N} k(N-k+1)
$$

Hence,
$$
N!^2 \geq NlgN\\
lgN! \geq \frac{1}{2}NlgN
$$

Hence $\frac{NlgN}{2}$ is bounded above by $N!$, so $O(NlgN) \subseteq O(lgN!)$ holds.

# 3. Prove that $O(lgN!) = O(NlgN)$ and $lgN! \in \Omega(NlgN)$
From 1, and 2, we have that:
$$
O(lgN!)\subseteq O(NlgN) \wedge O(NlgN) \subseteq O(lgN!)
$$
Thus:
$$
O(lgN!) = O(NlgN)
$$
Holds.

Additionally, given that $lgN! \geq \frac{1}{2} NlgN$, by $f(N) \geq c\cdot g(N) \forall N \geq N_0$, then $lgN! \in \Omega(NlgN)$.