# Two ways to cancel: Morken’s coprime Möbius sums

## The numbers that survive the sieve

Write the numbers from 1 to 10 and cross out the multiples of 2 or 5. Only 1, 3, 7 and 9 survive. Now give 1 a score of $+1$, 3 and 7 a score of $-1$ each, and 9 a score of $0$. The total is $-1$. Jamie Morken’s first question was whether the same score could be found by adding shorter sums attached to divisors of 10. The second asked whether it could be found using short sums with **no** crossing out. Both answers are yes, and neither requires the list to stop at 10.

Here is the scoring rule. If any prime is repeated in the factorization of $k$, give $k$ zero; otherwise give it $(-1)^s$, where $s$ is the number of prime factors. In particular 1 has score $1$, and $6=2\cdot3$ has score $1$. This is the Möbius function $\mu(k)$. Say two positive numbers are *coprime* when they have no common prime factor. Write $C_n(X)$ for the sum of the scores from 1 through $X$ of numbers coprime to $n$, and $M(X)$ for the sum with no filter. Let $\operatorname{rad}(q)$ be the product of the distinct primes of $q$, with $\operatorname{rad}(1)=1$. The diagonal $a(n)=C_n(n)$ is OEIS [A112399](https://oeis.org/A112399).

The two routes to $-1$ already show an important difference:

| Route for $n=X=10$ | Outer indices | Contributions in that order |
| --- | --- | --- |
| Squarefree divisors | $1,2,5,10$ | $-1,-1,0,1$ |
| Numbers using only primes of 10 | $1,2,4,5,8,10$ | $-1,-2,0,0,1,1$ |

Four and eight are not divisors of 10. They appear in the second row because their only prime is 2, which **does** divide 10.

::: {.film src="001-two-cancellations"}
Follow the score of a single term through both routes, then see why 4 and 8 belong in the second sum.
:::

## Why both sums work

::: {.theorem #thm-first-cutoff title="The squarefree-divisor identity" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" status="written-proof" proof="pf-first-cutoff" doi="10.5281/zenodo.24405799" source="Theorem 1, equation (1), Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/541"}
For integers $n\ge1$ and $X\ge0$, with only positive indices,
$$C_n(X)=\sum_{d\mid n,\,\mu(d)\ne0} C_d(\lfloor X/d\rfloor).$$
:::

::: {.proof #pf-first-cutoff}
In Ma and Zhang’s divisor route, an inner term indexed by $m$ with $(m,d)=1$ becomes a term at $k=dm$. Multiplying $\mu(dm)$ by $\mu(d)$ recovers $\mu(m)$ when $d$ is squarefree and $m$ shares no prime with it. If they share a prime, $dm$ has a repeated prime and both contributions vanish. Thus the net weight on $\mu(k)$ is $\sum_{d\mid(k,n)}\mu(d)$. If $k$ shares a prime $p$ with $n$, pair each squarefree $d$ not containing $p$ with $pd$; the signs cancel. If $k$ shares no prime with $n$, the only term is $d=1$. The change of index works because $m\le\lfloor X/d\rfloor$ is exactly $dm\le X$.
:::

::: {.theorem #thm-first-diagonal title="The first identity on the diagonal" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" lean="D5/S3/Arith/MoebiusLogarithmic/MorkenFirstDivisorSum.result"}
For integers $n\ge1$, $C_n(n)=\sum_{d\mid n,\,\mu(d)\ne0} C_d(\lfloor n/d\rfloor)$. This is the case $X=n$ of the preceding identity, not its full independent-cutoff form.
:::

::: {.theorem #thm-supported-cutoff title="The prime-supported Mertens identity" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" status="written-proof" proof="pf-supported-cutoff" doi="10.5281/zenodo.24405799" source="Theorem 1, equation (2), Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/542"}
For integers $n\ge1$ and $X\ge0$, with only positive indices,
$$C_n(X)=\sum_{q\le X,\,\operatorname{rad}(q)\mid n} M(\lfloor X/q\rfloor).$$
:::

::: {.proof #pf-supported-cutoff}
In the paper’s second route, fix the original index $r=qk$. For each $p^e$ exactly dividing $r$, ask how many powers of $p$ can go into $q$. If $p$ does not divide $n$, the only choice is zero copies of $p$, leaving factor $\mu(p^e)$. If $p$ divides $n$, all exponents from $0$ through $e$ are allowed. Only two choices give nonzero scores: leaving no copies in $k$ gives $+1$, and leaving one gives $-1$. They cancel. At $r=1$ the empty product is one. After this coefficient calculation, summing over $r\le X$ and collecting by $q$ gives the unrestricted sums $M(\lfloor X/q\rfloor)$.
:::

::: {.lemma #lem-supported-coefficient title="The pointwise prime-support coefficient" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" lean="D5/S3/Arith/MoebiusLogarithmic/CoprimeConvolution.sum_supported_moebius"}
For natural numbers $n,r$ (including zero), sum $\mu(r/q)$ over the natural divisors $q$ of $r$ for which every prime dividing $q$ divides $n$. The result is $\mu(r)$ if $(r,n)=1$ and zero otherwise. Here $0$ has the empty divisor list and $\mu(0)=0$. On positive inputs the filter is $\operatorname{rad}(q)\mid n$. This is the coefficient lemma used in the previous proof, not the finite sum over $r\le X$.
:::

Neither argument assumes $n$ is squarefree. In the first formula it is the **outer divisor** that must be squarefree, and the inner coprimality test uses $d$, not $n$. In the second, imposing $q\mid n$ would discard powers that are needed for the pairing. At $n=1$ both identities give $M(X)$; at $X=0$ every sum is empty.

::: {.slides src="overview"}
Seminar notes and slides: the two coefficient computations, the rectangle, and the boundaries of the result.
:::

## From one sum to a rectangle and a triangle

Consider a table with entry $\mu(jk)$ at row $j$ and column $k$. A prime shared by the row and column makes the entry zero. On the other cells, the entry is the product of their separate scores. This explains the product formula (even with a multiplicative weight) and gives a second use for the signed divisor filter: summing over a rectangle, group together pairs whose two indices are multiples of the same $d$. Each resulting block separates into a row sum and a column sum.

::: {.remark #cor-product title="Product formula with Bala’s multiplicative weight" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s2"}
For $n\ge1$, $X\ge0$ and a multiplicative arithmetic function $f$,
$$\sum_{k=1}^{X}\mu(nk)f(nk)=\mu(n)f(n)\sum_{k\le X,\,(k,n)=1}\mu(k)f(k).$$
In particular $f=1$ gives $\mu(n)C_n(X)$ for the unweighted sum. If $n$ is nonsquarefree both sides vanish; otherwise coprime terms factor and the rest vanish.
:::

::: {.corollary #cor-rectangle title="The rectangular quadratic identity" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s3" status="written-proof" proof="pf-rectangle" doi="10.5281/zenodo.24405799" source="Corollary 3, Section 2, Rectangular quadratic identity" request="https://github.com/the-omega-institute/trureturing-requests/issues/543"}
For integers $X,Y\ge0$,
$$\sum_{j=1}^{X}\sum_{k=1}^{Y}\mu(jk)=\sum_{d=1}^{\min(X,Y)}\mu(d)C_d(\lfloor X/d\rfloor)C_d(\lfloor Y/d\rfloor).$$
The square case $X=Y=N\ge1$ gives A372700, denoted $T(N)$ here.
:::

::: {.proof #pf-rectangle}
Expand the two short sums and put $j=du$, $k=dv$. Their terms become $\mu(d)\mu(j)\mu(k)$: for squarefree $d$ coprime to both $u,v$ the two factors of $\mu(d)$ square to one; other terms vanish. The weight at $(j,k)$ is now $\sum_{d\mid(j,k)}\mu(d)$, which keeps exactly the coprime pairs. There, $\mu(j)\mu(k)=\mu(jk)$, and at excluded pairs $\mu(jk)=0$. A zero side length gives empty sums.
:::

::: {.remark #cor-row title="Row sum and plateaux" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s4"}
For $N\ge1$, $T(N)=-1+2\sum_{k=1}^N\mu(k)a(k)$. Start at $T(1)=1$. For $N>1$ the extra row and column contribute $2\mu(N)a(N)$ by the product formula, since the corner $\mu(N^2)=0$. Thus $T(N)=T(N-1)$ whenever $N$ is nonsquarefree.
:::

The triangle $U(N,d)=C_d(\lfloor N/d\rfloor)$, for $1\le d\le N$, reads off exactly the short sums just used. Imagine keeping $d$ fixed and moving $N$ one step: no entry changes unless $d$ divides $N$, and then at most the endpoint $N/d$ enters. If $2d>N$, the only possible term is 1. Row totals have another interpretation: after writing $k=dm$, coprimality forces each full prime power of $k$ into one of the two factors. A prime occurring exactly once contributes the factor $1+\mu(p)=0$; a prime occurring at least twice contributes $1+0=1$. The unweighted row therefore counts *powerful* numbers up to $N$ (every prime exponent is at least two; 1 qualifies).

::: {.remark #cor-triangle title="Finite formulas of A400203" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s5"}
For $1\le d\le N$, the second identity gives $U(N,d)=\sum_{q\le N/d,\,\operatorname{rad}(q)\mid d}M(\lfloor N/(dq)\rfloor)$. Also $U(N,1)=M(N)$, $U(N,d)=1$ if $2d>N$ (in particular $U(N,N)=1$), and $U(N,d)=U(d\lfloor N/d\rfloor,d)$. For $d<N$ the increment $U(N,d)-U(N-1,d)$ is $\mu(N/d)$ if $d\mid N$ and $(N/d,d)=1$, zero otherwise.

The three row totals with weights $1,\mu(d),\mu(d)^2$ are respectively $\sum_{k\le N}H(k)=\mathrm{A217038}(N+1)$, $\sum_{k\le N}\mu(k)\tau(k)=\mathrm{A062563}(N)$, and $1$. Here $\tau(k)$ counts divisors. To see the last two, group by $k=dm$: the $\mu(d)$ weight gives $\mu(k)$ for each split of a squarefree $k$, zero otherwise; the $\mu(d)^2$ weight has local factors $\mu(p^e)+\mu(p^e)^2=0$ for all $e\ge1$.
:::

::: {.remark #cor-triangle-special title="Three recorded triangle specializations" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s11"}
For $n\ge1$, $a(n)=U(n^2,n)=\sum_{d\mid n,\,\mu(d)\ne0}U(n,d)$, and $\mathrm{A372706}(n)=\mu(n)U(n^2,n)$. These are respectively the defining cutoff $\lfloor n^2/n\rfloor=n$, the diagonal divisor identity, and the unweighted product formula.
:::

## Two small conventions that change answers

The indicator $H(k)$ for powerful numbers is not the sign of such a number. For $k=4$, $H(4)=1$ but $\mu(4)=0$. To give each distinct prime one minus sign, score the radical instead: $H(4)\mu(\operatorname{rad}(4))=-1$. At 1 both products are 1. This is the distinction behind the A112526 correction.

In the A304575 count, a strict inequality $k<d$ excludes the endpoint $k=d$. For $d>1$ that endpoint is not coprime to $d$ anyway, so nothing changes. But $d=1$ belongs to every divisor sum, and the strict count drops its lone term, worth 1. Already at $n=1$ the strict reading gives 0 and the inclusive reading gives 1.

::: {.remark #cor-signed title="A112526’s signed-variant convention" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s6"}
For positive $n$, $H(n)\mu(n)=\mathbf 1_{n=1}$. The distinct multiplicative function $H(n)\mu(\operatorname{rad}(n))$ has local value 0 at $p$ and $-1$ at $p^e$ for $e\ge2$. Evaluate at prime powers and use multiplicativity to recover its other values.
:::

::: {.corollary #cor-finite-transform title="A general finite transform" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s7" status="written-proof" proof="pf-finite-transform" doi="10.5281/zenodo.24405799" source="Corollary 7, Section 3, A general finite transform" request="https://github.com/the-omega-institute/trureturing-requests/issues/544"}
For $F:\mathbb Z_{>0}\to\mathbb C$, $n\ge1$ and $X\ge0$,
$$\sum_{k=1}^X F(k/(k,n))=\sum_{d\mid n}\sum_{m\le\lfloor Xd/n\rfloor,\,(m,d)=1}F(m).$$
At $X=n$, define $A_F(d)=\sum_{m\le d,\,(m,d)=1}F(m)$ and $B_F(n)=\sum_{k\le n}F(k/(k,n))$. Then $B_F(n)=\sum_{d\mid n}A_F(d)$ and $A_F(n)=\sum_{d\mid n}\mu(n/d)B_F(d)$.
:::

::: {.proof #pf-finite-transform}
Group by $g=(k,n)$, write $d=n/g$ and $k=gm$. The new numerator $m$ is coprime to $d$, and its cutoff is precisely $\lfloor Xd/n\rfloor$. Conversely such a pair gives back $k=gm$ with gcd exactly $g$. At the diagonal the smaller cutoff is $d$. For its inverse, substitute the divisor sum and use $\sum_{e\mid t}\mu(e)=\mathbf1_{t=1}$.
:::

::: {.remark #cor-mobius-transform title="The A332685 transform and its inverse" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s8"}
Let $b(n)=\sum_{k\le n}\mu(k/(k,n))$. With $F=\mu$, the diagonal transform gives $b(n)=\sum_{d\mid n}a(d)$ and $a(n)=\sum_{d\mid n}\mu(n/d)b(d)$. The argument $k/(k,n)$ can also be written $\operatorname{lcm}(n,k)/n$.
:::

::: {.remark #cor-counts title="Squarefree counts and the A304575 endpoint" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s9"}
For $s(d)=\sum_{k\le d,\,(k,d)=1}\mu(k)^2$, the inclusive total $R(n)=\sum_{d\mid n}s(d)$ equals $\sum_{k\le n}\mu(k/(k,n))^2$, hence also the version with $\operatorname{lcm}(n,k)/n$. Thus $R(n)\le n$, $s(n)=\sum_{d\mid n}\mu(n/d)R(d)$, and replacing the inclusive endpoint by a strict one gives $R(n)-1$.

Put $Q(t)=\sum_{1\le k<t}\mu(k)^2$. For primes $p$ and integers $m\ge0$, $R(p^{2m})=1+\sum_{i=0}^m Q(p^{2i})$ and $R(p^{2m+1})=1+\sum_{i=0}^m Q(p^{2i+1})$. With $D_j=s(p^j)$, splitting the numbers counted by $Q(p^j)$ according to divisibility by $p$ gives $D_j+D_{j-1}=Q(p^j)$ for $j\ge2$. Pair successive terms in $\sum_{j=0}^e D_j$, using $D_0=1$, $D_1=Q(p)$ and $Q(1)=0$.
:::

::: {.remark #cor-gcd title="Other finite gcd sums" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s10"}
For $n\ge1$ and any arithmetic function $F$, the $\varphi(n/d)$ choices with gcd $d$ give $\sum_{k\le n}F((k,n))=\sum_{d\mid n}F(d)\varphi(n/d)$ and $\sum_{k\le n}F(n/(k,n))=\sum_{d\mid n}F(d)\varphi(d)$. Here $\varphi(m)$ counts the positive integers at most $m$ that are coprime to $m$.

At a prime power $p^e$ with $e\ge1$, A007431 has factor $\varphi(p^e)-\varphi(p^{e-1})$ (that is $p-2$ if $e=1$, $p^{e-2}(p-1)^2$ otherwise); A063659 has $\varphi(p^e)+\varphi(p^{e-1})$ ($p$ if $e=1$, $p^e-p^{e-2}$ otherwise). These come from using $F=\mu$ and $F=\mu^2$. With $F=\mu$ in the quotient formula one gets A276833$(n)=\prod_{p\mid n}(2-p)$. Finally $\sum_{d\mid n}\mathrm{A007431}(d)=\varphi(n)$ by the Möbius divisor filter.
:::

## What the paper proves, and what it doesn’t

These are identities of **finite** sums. They give different exact ways to compute the same numbers; they do not prove infinitely many sign changes for A372700 or asymptotic cancellation estimates. The public Lean source proves the first identity on the diagonal $X=n>0$ and proves the second identity’s pointwise coefficient formula. The diagonal does not give the independent-cutoff first formula as stated, and the coefficient theorem is not itself the finite reindexing step giving the second formula. The paper supplies both written arguments.

**Sources.** [Haobo Ma and Wenlin Zhang, version 3](https://doi.org/10.5281/zenodo.24405799), §§1–3. Jamie Morken posed the diagonal problems in A112399, revision 41, FORMULA (September 18, 2026). The paper credits Sander–Sander (2009, proof of Proposition 4) and Ramaré (2014, §1) for prior forms of the first identity, and Ramaré (online December 1, 2014; print 2015, equation 16.1) for an equivalent second identity. It also credits Helfgott’s coefficient calculation, Peter Bala’s weighted product proof, West’s reduced-fraction transform and Schramm’s gcd sums. Morken recorded the triangle formulas on September 21, 2026; the later revision-17 snapshot is not their first appearance.
