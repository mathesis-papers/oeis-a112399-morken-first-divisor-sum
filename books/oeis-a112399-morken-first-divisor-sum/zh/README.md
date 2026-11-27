# 两种消去法：Morken 的互素莫比乌斯和

## 筛完以后还剩什么？

写下 1 到 10，划去 2 或 5 的倍数，只剩下 1、3、7、9。给 1 记 $+1$ 分，给 3 和 7 各记 $-1$ 分，给 9 记 $0$ 分，总分就是 $-1$。Jamie Morken 提出了两个问题：能不能把这个结果拆成几个与 10 的因数有关的短和？能不能用完全**不筛选**的短和得到同一个结果？两个问题的答案都是肯定的，而且数列不必写到 10 就停。

计分规则是：若 $k$ 的质因数分解中有重复的质数，就记 0 分；否则记 $(-1)^s$ 分，其中 $s$ 是不同质因数的个数。因此 1 记 1 分，$6=2\cdot3$ 也记 1 分。这个分数记作 $\mu(k)$，称为莫比乌斯函数。没有共同质因数的两个数称为*互素*。记 $C_n(X)$ 为从 1 到 $X$ 中与 $n$ 互素的数的分数之和，$M(X)$ 为不加筛选的总分。记 $\operatorname{rad}(q)$ 为 $q$ 的不同质因数的乘积，并约定 $\operatorname{rad}(1)=1$。取 $X=n$ 得到的 $a(n)=C_n(n)$ 就是 OEIS [A112399](https://oeis.org/A112399)。

在 $n=X=10$ 时，两条路都得到 $-1$，但所用的下标不同：

| 方法 | 外层下标 | 按顺序列出的贡献 |
| --- | --- | --- |
| 只用无平方因子的因数 | $1,2,5,10$ | $-1,-1,0,1$ |
| 只用质因数都来自 10 的数 | $1,2,4,5,8,10$ | $-1,-2,0,0,1,1$ |

4 和 8 不是 10 的因数，却出现在第二行，因为它们唯一的质因数 2 整除 10。

::: {.film src="001-two-cancellations"}
跟着同一个下标走两条计分路线，看看为何第二个和式不能漏掉 4 与 8。
:::

## 两个和式为什么成立？

::: {.theorem #thm-first-cutoff title="无平方因子的因数恒等式" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" status="written-proof" proof="pf-first-cutoff" doi="10.5281/zenodo.24405799" source="Theorem 1, equation (1), Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/541"}
对整数 $n\ge1$、$X\ge0$，求和下标均为正数，有
$$C_n(X)=\sum_{d\mid n,\,\mu(d)\ne0} C_d(\lfloor X/d\rfloor).$$
:::

::: {.proof #pf-first-cutoff}
Ma 和 Zhang 的第一种证明把内层的下标 $m$ 换成 $k=dm$。若 $d$ 无平方因子且 $(m,d)=1$，则 $\mu(dm)$ 乘上 $\mu(d)$ 正好还原 $\mu(m)$。若二者有共同质因数，$dm$ 含有质数的平方，相应贡献为零。因此，$\mu(k)$ 的系数为 $\sum_{d\mid(k,n)}\mu(d)$。只要 $k$ 与 $n$ 有共同质因数 $p$，就可以把不含 $p$ 的无平方因子 $d$ 与 $pd$ 配对，符号恰好相反；没有共同质因数时，只剩下 $d=1$。换下标不会丢掉边界，因为 $m\le\lfloor X/d\rfloor$ 等价于 $dm\le X$。
:::

::: {.theorem #thm-first-diagonal title="第一式的对角线情形" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" lean="D5/S3/Arith/MoebiusLogarithmic/MorkenFirstDivisorSum.result"}
对整数 $n\ge1$，$C_n(n)=\sum_{d\mid n,\,\mu(d)\ne0} C_d(\lfloor n/d\rfloor)$。这是上一个恒等式取 $X=n$ 的情形，不是截点可以独立变化的一般形式。
:::

::: {.theorem #thm-supported-cutoff title="限制质因数的默滕斯和恒等式" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" status="written-proof" proof="pf-supported-cutoff" doi="10.5281/zenodo.24405799" source="Theorem 1, equation (2), Section 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/542"}
对整数 $n\ge1$、$X\ge0$，求和下标均为正数，有
$$C_n(X)=\sum_{q\le X,\,\operatorname{rad}(q)\mid n} M(\lfloor X/q\rfloor).$$
:::

::: {.proof #pf-supported-cutoff}
论文的第二种证明固定原下标 $r=qk$，再看 $r$ 中每个恰好出现 $e$ 次的质因数 $p$。若 $p$ 不整除 $n$，它的所有副本都得留给 $k$，贡献因子 $\mu(p^e)$。若 $p$ 整除 $n$，可以把 $0$ 到 $e$ 个副本分给 $q$。只有两种分法的得分不为零：给 $k$ 留零个得 $+1$，留一个得 $-1$；二者抵消。$r=1$ 时空乘积等于 1。把算出的系数对 $r\le X$ 求和，再按 $q$ 归类，就得到不带互素条件的 $M(\lfloor X/q\rfloor)$。
:::

::: {.lemma #lem-supported-coefficient title="限制质因数时的逐项系数" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s1" lean="D5/S3/Arith/MoebiusLogarithmic/CoprimeConvolution.sum_supported_moebius"}
对自然数 $n,r$（也可取零），将 $\mu(r/q)$ 对 $r$ 的因数 $q$ 求和，条件是整除 $q$ 的每个质数都整除 $n$。若 $(r,n)=1$，结果为 $\mu(r)$；否则为零。这里约定零的因数列表为空，且 $\mu(0)=0$。在正数上，筛选条件等价于 $\operatorname{rad}(q)\mid n$。这正是上一证明中的单项系数，不是对 $r\le X$ 的有限和。
:::

两种证明都不要求 $n$ 无平方因子。第一式的限制落在**外层因数** $d$ 上，内层要与 $d$ 互素，而不是与 $n$ 互素。第二式若要求 $q\mid n$，就会漏掉配对所需的质数幂。$n=1$ 时两式都等于 $M(X)$；$X=0$ 时所有和式都是空和。

::: {.slides src="overview"}
英文报告与讲者备注：两种系数算法、矩形公式和结论的适用范围。
:::

## 从一条和式到矩形和三角阵

画一张表，第 $j$ 行第 $k$ 列填入 $\mu(jk)$。如果行号和列号有共同质因数，格子的分数就是零；否则是二者分数的乘积。这说明了乘积公式为何成立，也说明了为什么可以加入积性权重。对矩形求和时，可以再次使用带符号的因数筛：按照同时整除行号和列号的 $d$ 归类，每一块都可拆成行、列两个短和的乘积。

::: {.remark #cor-product title="Bala 的积性带权乘积公式" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s2"}
对 $n\ge1$、$X\ge0$ 和积性算术函数 $f$，
$$\sum_{k=1}^{X}\mu(nk)f(nk)=\mu(n)f(n)\sum_{k\le X,\,(k,n)=1}\mu(k)f(k).$$
特别地，令 $f=1$，无权和就是 $\mu(n)C_n(X)$。若 $n$ 含平方因子，两边均为零；否则互素项由积性拆开，其余项为零。
:::

::: {.corollary #cor-rectangle title="矩形二次恒等式" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s3" status="written-proof" proof="pf-rectangle" doi="10.5281/zenodo.24405799" source="Corollary 3, Section 2, Rectangular quadratic identity" request="https://github.com/the-omega-institute/trureturing-requests/issues/543"}
对整数 $X,Y\ge0$，
$$\sum_{j=1}^{X}\sum_{k=1}^{Y}\mu(jk)=\sum_{d=1}^{\min(X,Y)}\mu(d)C_d(\lfloor X/d\rfloor)C_d(\lfloor Y/d\rfloor).$$
取 $X=Y=N\ge1$ 就得到 A372700，这里记作 $T(N)$。
:::

::: {.proof #pf-rectangle}
展开两个短和，令 $j=du$、$k=dv$。各项可改写为 $\mu(d)\mu(j)\mu(k)$：当 $d$ 无平方因子且分别与 $u,v$ 互素时，两个 $\mu(d)$ 相乘得一；其余项为零。此时 $(j,k)$ 的权重为 $\sum_{d\mid(j,k)}\mu(d)$，恰好留下互素的配对。对这些配对有 $\mu(j)\mu(k)=\mu(jk)$，而被筛去的配对满足 $\mu(jk)=0$。任一边长为零时，两边都是空和。
:::

::: {.remark #cor-row title="行和及平台" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s4"}
对 $N\ge1$，$T(N)=-1+2\sum_{k=1}^N\mu(k)a(k)$。初值是 $T(1)=1$。当 $N>1$ 时，用乘积公式计算增加的一行一列；因角上的 $\mu(N^2)=0$，增加量为 $2\mu(N)a(N)$。所以当 $N$ 含有平方因子时，$T(N)=T(N-1)$。
:::

三角阵 $U(N,d)=C_d(\lfloor N/d\rfloor)$（$1\le d\le N$）把这些短和逐个列出。固定 $d$，让 $N$ 增加 1：只有 $d$ 整除新 $N$ 时才可能改变，而且最多新增端点 $N/d$。若 $2d>N$，唯一可能出现的内层项就是 1。对整行求和还有一个数数的解释：写成 $k=dm$ 后，由于 $d$ 和 $m$ 互素，每个完整的质数幂只能放入其中一边。只出现一次的质数给出因子 $1+\mu(p)=0$；出现至少两次的质数给出 $1+0=1$。所以无权行和数的是不超过 $N$ 的*幂强数*：每个质因数的指数都至少为二，1 也算在内。

::: {.remark #cor-triangle title="A400203 的有限公式" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s5"}
对 $1\le d\le N$，第二式给出 $U(N,d)=\sum_{q\le N/d,\,\operatorname{rad}(q)\mid d}M(\lfloor N/(dq)\rfloor)$。此外 $U(N,1)=M(N)$，当 $2d>N$ 时 $U(N,d)=1$（特别是 $U(N,N)=1$），而且 $U(N,d)=U(d\lfloor N/d\rfloor,d)$。若 $d<N$，增量 $U(N,d)-U(N-1,d)$ 在 $d\mid N$ 且 $(N/d,d)=1$ 时为 $\mu(N/d)$，否则为零。

权重取 $1,\mu(d),\mu(d)^2$ 时，三种行和依次为 $\sum_{k\le N}H(k)=\mathrm{A217038}(N+1)$、$\sum_{k\le N}\mu(k)\tau(k)=\mathrm{A062563}(N)$ 和 $1$，其中 $\tau(k)$ 是正因数个数。后两式也可按 $k=dm$ 分组：权重为 $\mu(d)$ 时，无平方因子的 $k$ 的每种拆法都贡献 $\mu(k)$，其余为零；权重为 $\mu(d)^2$ 时，每个 $e\ge1$ 的局部因子 $\mu(p^e)+\mu(p^e)^2$ 都为零。
:::

::: {.remark #cor-triangle-special title="已记录的三个三角阵特例" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s11"}
对 $n\ge1$，$a(n)=U(n^2,n)=\sum_{d\mid n,\,\mu(d)\ne0}U(n,d)$，且 $\mathrm{A372706}(n)=\mu(n)U(n^2,n)$。三式分别来自截点 $\lfloor n^2/n\rfloor=n$、对角线上的因数恒等式和无权乘积公式。
:::

## 两处会改变答案的约定

幂强数的指示函数 $H(k)$ 不是该数的符号。例如 $H(4)=1$，但 $\mu(4)=0$。若要让每个不同质因数提供一个负号，应当对根基数计分：$H(4)\mu(\operatorname{rad}(4))=-1$。在 1 处两个乘积都等于 1。这就是 A112526 的修正。

A304575 中的严格不等式 $k<d$ 会排除端点 $k=d$。当 $d>1$ 时，这个端点本来就不与 $d$ 互素，所以没有影响。但 $d=1$ 出现在每次因数求和中，严格不等式却删掉了它唯一的一项，恰好少算 1。只看 $n=1$ 就能发现：严格版本得到 0，包含端点的版本得到 1。

::: {.remark #cor-signed title="A112526 的带符号版本约定" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s6"}
对正整数 $n$，$H(n)\mu(n)=\mathbf 1_{n=1}$。另一个积性函数 $H(n)\mu(\operatorname{rad}(n))$ 在 $p$ 处取零，在 $p^e$（$e\ge2$）处取 $-1$。先算质数幂上的值，再由积性得到其余值。
:::

::: {.corollary #cor-finite-transform title="一般的有限变换" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s7" status="written-proof" proof="pf-finite-transform" doi="10.5281/zenodo.24405799" source="Corollary 7, Section 3, A general finite transform" request="https://github.com/the-omega-institute/trureturing-requests/issues/544"}
对 $F:\mathbb Z_{>0}\to\mathbb C$、$n\ge1$、$X\ge0$，
$$\sum_{k=1}^X F(k/(k,n))=\sum_{d\mid n}\sum_{m\le\lfloor Xd/n\rfloor,\,(m,d)=1}F(m).$$
当 $X=n$ 时，记 $A_F(d)=\sum_{m\le d,\,(m,d)=1}F(m)$、$B_F(n)=\sum_{k\le n}F(k/(k,n))$。于是 $B_F(n)=\sum_{d\mid n}A_F(d)$，且 $A_F(n)=\sum_{d\mid n}\mu(n/d)B_F(d)$。
:::

::: {.proof #pf-finite-transform}
按 $g=(k,n)$ 分组，写 $d=n/g$、$k=gm$。新分子 $m$ 与 $d$ 互素，其截点正是 $\lfloor Xd/n\rfloor$。反过来，每个这样的配对都给出 $k=gm$，且最大公因数恰为 $g$。在对角线上，小截点为 $d$。求逆时，把因数和式代入并使用 $\sum_{e\mid t}\mu(e)=\mathbf1_{t=1}$ 即可。
:::

::: {.remark #cor-mobius-transform title="A332685 的变换及逆变换" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s8"}
记 $b(n)=\sum_{k\le n}\mu(k/(k,n))$。取 $F=\mu$，对角线变换给出 $b(n)=\sum_{d\mid n}a(d)$ 和 $a(n)=\sum_{d\mid n}\mu(n/d)b(d)$。其中 $k/(k,n)$ 也可写成 $\operatorname{lcm}(n,k)/n$。
:::

::: {.remark #cor-counts title="无平方因子的计数与 A304575 的端点" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s9"}
令 $s(d)=\sum_{k\le d,\,(k,d)=1}\mu(k)^2$。包含端点的计数 $R(n)=\sum_{d\mid n}s(d)$ 等于 $\sum_{k\le n}\mu(k/(k,n))^2$，也等于将其中的自变量换成 $\operatorname{lcm}(n,k)/n$ 的和。因此 $R(n)\le n$、$s(n)=\sum_{d\mid n}\mu(n/d)R(d)$，而采用严格端点得到的是 $R(n)-1$。

记 $Q(t)=\sum_{1\le k<t}\mu(k)^2$。对质数 $p$ 和整数 $m\ge0$，有 $R(p^{2m})=1+\sum_{i=0}^m Q(p^{2i})$ 和 $R(p^{2m+1})=1+\sum_{i=0}^m Q(p^{2i+1})$。令 $D_j=s(p^j)$，把 $Q(p^j)$ 计数的对象按是否被 $p$ 整除分两类，得到 $D_j+D_{j-1}=Q(p^j)$（$j\ge2$）。利用 $D_0=1$、$D_1=Q(p)$、$Q(1)=0$，把 $\sum_{j=0}^e D_j$ 中相邻项配对即可。
:::

::: {.remark #cor-gcd title="其他有限最大公因数和式" mathesis="collected:oeis-a112399-morken-first-divisor-sum:3:s10"}
对 $n\ge1$ 和任意算术函数 $F$，最大公因数为 $d$ 的选择有 $\varphi(n/d)$ 个，故 $\sum_{k\le n}F((k,n))=\sum_{d\mid n}F(d)\varphi(n/d)$，且 $\sum_{k\le n}F(n/(k,n))=\sum_{d\mid n}F(d)\varphi(d)$。这里 $\varphi(m)$ 数的是不超过 $m$ 且与 $m$ 互素的正整数。

在质数幂 $p^e$（$e\ge1$）处，A007431 的因子为 $\varphi(p^e)-\varphi(p^{e-1})$（$e=1$ 时为 $p-2$，其余为 $p^{e-2}(p-1)^2$）；A063659 的因子为 $\varphi(p^e)+\varphi(p^{e-1})$（$e=1$ 时为 $p$，其余为 $p^e-p^{e-2}$）。这分别来自 $F=\mu$ 和 $F=\mu^2$。在第二个和式取 $F=\mu$，还得到 A276833$(n)=\prod_{p\mid n}(2-p)$。最后用莫比乌斯因数筛可得 $\sum_{d\mid n}\mathrm{A007431}(d)=\varphi(n)$。
:::

## 结论的范围和来源

这些都是**有限和**的恒等式。它们给出了精确计算同一个数的不同办法，却没有证明 A372700 会无穷多次变号，也没有给出渐近估计。公开的 Lean 源码证明了第一式在 $X=n>0$ 时的情形，以及第二式所用的逐项系数恒等式。前者没有把截点 $X$ 与参数 $n$ 分开；后者也不是把系数求和、换下标后得到的完整第二式。论文给出了这两个步骤的书面证明。

**来源。** [Haobo Ma 和 Wenlin Zhang，第 3 版](https://doi.org/10.5281/zenodo.24405799)，第 1–3 节。Jamie Morken 在 2026 年 9 月 18 日的 A112399 第 41 次修订（FORMULA）中提出对角线上的两个问题。论文指出，第一式已有 Sander–Sander（2009，命题 4 的证明）和 Ramaré（2014，第 1 节）的相关形式；第二式的等价形式见 Ramaré（2014 年 12 月 1 日在线发表，2015 年印刷，式 16.1）。论文也说明了 Helfgott 的系数公式、Peter Bala 的带权乘积证明、West 的既约分数变换以及 Schramm 的最大公因数和式。Morken 在 2026 年 9 月 21 日记下三角阵的公式；后来的第 17 次修订并不是这些公式的首次出现。
