# Convention corrections and alternative proofs for Morken's A112399 conjectures

The note gives self-contained alternative proofs of the two identities in the
FORMULA section of OEIS A112399, revision 41, including arbitrary cutoffs,
following Sander–Sander (2009) and Ramaré (2014–2015). Its corollaries cover all
finite formulas in A400203 revision 17 and its three triangle specializations
recorded on 21 September 2026, a rectangular A372700 identity,
arbitrary-function divisor grouping, and the nearby squarefree-count and gcd
transforms. Earlier proofs and recorded formulas are distinguished explicitly.

Two source conventions are corrected: the literal strict endpoint in A304575
is one below its data and inclusive formulas; the signed-variant comment in
A112526 needs the Möbius function of the radical, rather than of the integer.

## Earlier proofs

- Sander and Sander (2009), proof of Proposition 4, equations (5)–(7): the finite coprimality expansion specializes to the first identity and supplies the rectangular cancellation.
- Ramaré (2014), section 1 after (1.2): a reciprocal-weight form equivalent to the first identity; Ramaré (electronically 1 December 2014, print 2015), section 16, (16.1): the second identity after the unique reindexing `q=d*w^2`.
- Ingix/reuns (13 June 2019) and Helfgott (December 2019), section 5.3.4: coefficient proofs.
- Ramaré–Zuniga-Alterman, arXiv:2603.25961, Lemma 2.5, and Zuniga-Alterman, arXiv:2610.17720, Lemma 7.1: later general coefficient and weighted statements; the latter appeared on 13 October and was revised on 26 October 2026.
- West (2013): the general diagonal divisor transform; Schramm (2008): the general finite gcd formula. Bala (22 September 2026), Proposition 1: the weighted product identity.

Exact sources and locators are included in the note's bibliography and coverage
table. The identities are presented as alternative proofs and a consolidation
of the specified finite formulas, rather than as priority claims.

## Contents

- `note.tex`: self-contained LaTeX source with the bibliography included.
- `note.pdf`: readable mathematical note, supplied alongside the source archive.
- `metadata.json`: title, authors, license, problem identifier and Lean source.
- `verify.py`: Python 3 finite checker, using only the standard library.
- `verification.json`: exact finite-check results and checker hash.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard LaTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in `note.tex`; BibTeX is unnecessary.

## Check the identities

```sh
python3 verify.py --output verification.json
```

The finite ranges and integer comparisons are listed in `verification.json`.
The all-input arguments are the written proofs in the note. The pinned Lean
declaration `D5.S3.Arith.MoebiusLogarithmic.MorkenFirstDivisorSum.result`
proves the first identity for every positive `n` with cutoff `X=n`:

https://github.com/the-omega-institute/trureturing/blob/4a11a6467d4ba3682c7630cd22c551cd11074cc6/D5/S3/Arith/MoebiusLogarithmic/MorkenFirstDivisorSum.lean

At the same revision, `D5.S3.Arith.MoebiusLogarithmic.sum_supported_moebius`
proves the prime-supported coefficient identity used for the second conjecture:

https://github.com/the-omega-institute/trureturing/blob/4a11a6467d4ba3682c7630cd22c551cd11074cc6/D5/S3/Arith/MoebiusLogarithmic/CoprimeConvolution.lean

The finite summation giving the second conjecture, the arbitrary-cutoff formulas,
and every numbered corollary are supplied with written proofs. Exact checks
include 7,260 main cutoff pairs, 1,681 rectangles, 10,650 arbitrary-function
grouping comparisons, all 12,880 triangle entries through row 160, the new
finite transforms through 200, and every prime power at most 200.
The A372700 sign-change conjecture is not covered. The coverage table gives
the exact source locators for proved formulas, corrected statements, the
previously proved product formula, and statements outside coverage.

## Attribution and license

Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang
(National University of Singapore; ChronoAI Pte Ltd, Singapore).
CC BY 4.0 (`cc-by-4.0`). The conjectures are attributed to Jamie Morken in
OEIS A112399. Peter Bala's 22 September 2026 proof concerns the product identity
in A372706; the note cites that proof explicitly.
