# Simpson-Regularized Harmonic Sum and Delta Estimation

This repository provides a Python implementation for computing a Simpson-regularized approximation of the harmonic sum and estimating the constant

\[
\delta = \gamma - \left(\frac{\log 2}{3} + \frac{1}{3}\right),
\]

where \(\gamma\) is the Euler–Mascheroni constant.

---

## Overview

We define the local Simpson weight

\[
g(k) = \frac{1}{3}
\left(
\frac{1}{2k-1}
+
\frac{4}{2k}
+
\frac{1}{2k+1}
\right),
\]

which corresponds to Simpson's rule on the interval \([2k-1, 2k+1]\).

Using this, we construct a global approximation \(h(N)\):

- For odd \(N\):

\[
h(N) = \sum_{k=1}^{\frac{N-1}{2}} g(k)
\]

- For even \(N\):

\[
h(N) = h(N-1) +
\frac{1}{6}
\left(
\frac{1}{N-1}
+
\frac{4}{N - \tfrac{1}{2}}
+
\frac{1}{N}
\right)
\]

---

## Delta Approximation

We estimate

\[
a(N) = 2h(N) - h(N^2).
\]

This quantity converges to \(\delta\) as \(N \to \infty\).

---

## Error Bound

We define an upper bound \(r(N)\) as:

- If \(N\) is odd:

\[
r(N) = \frac{1}{15 (N-1)^4}
\]

- If \(N\) is even:

\[
r(N) =
\frac{1}{15 (N-2)^4}
+
\frac{1}{120 (N-1)^5}.
\]

---

## Output

The script outputs tab-separated values with the following columns:

``
