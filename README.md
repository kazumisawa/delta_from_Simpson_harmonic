# Simpson-Type Decomposition of the Euler-Mascheroni Constant

This repository contains the source code used in the paper

    "A Simpson-Type Decomposition of the Euler-Mascheroni Constant"

and provides scripts to reproduce all numerical results reported in the manuscript.

## Simpson-Type Approximation

We define the local Simpson weight

\[
g(k)=\frac{1}{3}\left(
\frac{1}{2k-1}
+\frac{4}{2k}
+\frac{1}{2k+1}
\right),
\]

which corresponds to Simpson's rule applied to the interval
\([2k-1,\,2k+1]\).

Using these local weights, we define the global approximation \(h(N)\).

For odd \(N\),

\[
h(N)=\sum_{k=1}^{(N-1)/2} g(k).
\]

For even \(N\),

\[
h(N)
=
h(N-1)
+
\frac{1}{6}
\left(
\frac{1}{N-1}
+
\frac{4}{N-\tfrac12}
+
\frac{1}{N}
\right).
\]

The main result of the paper is that

\[
\lim_{N\to\infty}
\left(
h(N)-\log N
\right)
=
\gamma,
\]

where \(\gamma\) denotes the Euler-Mascheroni constant.

## Contents

- `newTable2.py`
  
  Reproduces Table 2 of the manuscript, including both odd and even values of \(N\), and evaluates their convergence behavior.

- `newTable3.py`
  
  Reproduces Table 3 of the manuscript and compares the convergence rates of the proposed Simpson-type approximation with previously published approximations to \(\gamma\).

## Reproducibility

All numerical values reported in Tables 2 and 3 can be reproduced directly from the scripts included in this repository.

