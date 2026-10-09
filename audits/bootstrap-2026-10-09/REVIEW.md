# Claim audit: bootstrap blog post

Reviewed 9 October 2026. Post: “Where a confidence interval comes from”, dated 8 October 2026. The blog index confirms this is the latest local post.

## Outcome and scope

The pilot calculations, published interval endpoints, coverage table, simulation widths, R example and default figure readouts reproduce at the precision reported. The statistical explanation of the ordinary two-sample bootstrap and the small-sample percentile problem is supported. This does **not** establish that every recommendation is valid without further conditions.

The consolidated findings below contain four corrections and one methodological qualification. They remain open in the article. This was a review: the article and its exports were not edited. The persistent review rule was added to `AGENTS.md`, and calculation scripts and fresh outputs were saved under this audit's `evidence/` directory.

Scope: current HTML article (including its latest wording), exported Markdown, embedded Markdown, downloadable PDF, static SVG figures, interactive figure calculations, five tables, example code, bibliography, and claims about linked earlier posts that this article relies on. The earlier posts were checked for those dependencies, not audited in full. Local source hashes are recorded in `evidence/checks.json`.

## Consolidated findings

### F1 — Corrected HTML has stale exports and an empty offline Markdown copy

**Correction; priority 2.** The source HTML contains changes absent from the downloaded Markdown and PDF: a more precise explanation of BCa acceleration; qualifications about median intervals; conditioning on observed group sizes; residual-bootstrap model and variance assumptions; and the extended Hesterberg reference. The precise Markdown differences are in `evidence/export-diff.txt`. The current source text is captured in `evidence/current-source.md`.

The embedded `pt-md` textarea is empty. When fetching the Markdown fails, the copy handler uses this empty value. A browser execution with clipboard capture confirms that “Copy as Markdown” copies a string of length zero on the local-file fallback path (`evidence/second-round.json`).

**Action:** after the substantive wording corrections below, run `python3 tools/export_post.py bootstrap`. Check the resulting Markdown, PDF, SVGs and embedded text against the HTML. The regression qualification already exists in the current HTML; do not reopen it as a source-text defect. It still needs to reach the exports.

### F2 — Independence is stated as a requirement for every bootstrap

**Correction; priority 2.** Section 6 says resampling units need to be independent. That describes the ordinary independent-observation bootstrap, but is too broad for the time-series bootstrap recommended in Table 4. Consecutive blocks can preserve dependence without making the original observations, or adjacent/overlapping blocks, independent. Validity then requires appropriate dependence conditions and a suitable block scheme and length.

**Action:** scope the independence statement to the ordinary bootstrap, then explain that dependent data require a resampling scheme preserving the relevant dependence. Qualify the time-series row as applying to an appropriate stationary/weakly dependent setting with a justified block length; “blocks” alone is not a complete method. The original Künsch full text was inaccessible in this audit; the publisher's [stationary-bootstrap abstract](https://www.tandfonline.com/doi/abs/10.1080/01621459.1994.10476870) independently supports the distinction between dependence and independence.

### F3 — The direction of the wrong-unit error is overstated

**Correction; priority 2.** Section 9.2 states that treating correlated measurements independently makes intervals too narrow. This often happens for a mean with positive clustering, but the direction depends on the estimand and covariance. For a paired before–after difference, positive within-person correlation reduces the variance of the difference. Breaking the pairing can therefore inflate uncertainty.

A direct counterexample, calculated in `evidence/checks.json`: with marginal variances 1, correlation 0.8 and 10 independent pairs, the variance of the mean paired difference is `(1 + 1 − 2 × 0.8)/10 = 0.04`. Ignoring the covariance gives `2/10 = 0.20`, five times as large, with a standard error larger by `sqrt(5) = 2.236`. The rule to preserve participants/pairs remains correct; the unconditional direction claim does not.

Section 9.3 also states without qualification that omitting data-driven steps makes an interval too narrow. What follows generally is that it measures a different procedure's uncertainty; a universally narrower interval does not follow.

**Action:** say that breaking the dependence structure or omitting adaptive steps can misrepresent uncertainty, often underestimating it, and that the direction depends on the statistic and procedure. Preserve the advice to resample the correct units and repeat the relevant analysis steps.

### F4 — Table 5's simulation provenance and “ideal” labels need clarification

**Correction to documentation; priority 3.** The reported ranges reproduce, but the post does not state the number of independent runs used to estimate each range or the seed. Those runs themselves have Monte Carlo uncertainty. The recovered script uses seed 12, with 4,000, 2,000 and 400 runs for 999, 9,999 and 99,999 resamples respectively. A fresh rerun reproduces every displayed range at its reported precision (`evidence/monte_carlo.txt`). Its within-run quantiles use `boot:::norm.inter`; the outer central ranges use R's type-1 quantiles.

The bootstrap-t endpoints in the “Ideal” row are high-precision simulation estimates, not exact enumeration. Table 2 already says they were estimated with 10 million draws, but Table 5's label and the later reference to “ideal 0.5 to 14.6” should carry that distinction explicitly.

**Action:** add the outer run counts, seed, quantile conventions and a footnote distinguishing exact percentile/SE values from the simulated approximation to the ideal bootstrap-t interval. Link durable calculation code. This audit preserves the recovered scripts; it does not add a link to them in the article.

### F5 — Repeating variable selection is not sufficient to validate post-selection intervals

**Methodological qualification; priority 3.** Table 4, Section 9.3 and the checklist correctly advise repeating data-dependent steps when estimating uncertainty for the whole procedure. Add a qualification that this is not, by itself, a validity guarantee. Discontinuous selection or thresholding can create nonregular inference problems even when the complete procedure is repeated.

**Action:** add a short sentence requiring method-specific justification for post-selection confidence intervals and other nonregular statistics. Do not claim that all such bootstraps fail: the limitation depends on the selection procedure, target and setting. [Leeb and Pötscher's primary research](https://arxiv.org/abs/0704.1584) establishes limits on uniformly accurate estimation of post-model-selection distributions in the settings they analyse.

## Claim-by-claim verification ledger

Repeated statements in the abstract, captions, tables and traps were checked against the same calculation rather than treated as independent evidence. “Verified” means supported at the stated scope and precision; it does not mean that all extrapolations are valid.

| Location and claim | Evidence and result |
|---|---|
| Summary and Section 1: sampling distribution, SE and confidence-procedure interpretation | Verified for the stated repeated-sampling model. Coverage is a property of the procedure. The distinction from an interval-specific probability is maintained. |
| Section 1: illustrative trial, 20 people, 10 per arm, 12 weeks | The data are explicitly fictional. Arrays and trial description match the previous permutation post. No real clinical study is claimed. |
| Table 1: means and SDs | Recomputed: 9.4 and 1.9; sample SDs 7.734483 and 7.140650, rounding to 7.7 and 7.1. |
| Section 1 and Table 2: pooled t SE, df, critical value and limits | Recomputed: SE 3.328830, df 18, limits 0.506387–14.493613. Normal equal-variance model gives the t pivot; the raw difference has a normal sampling distribution. |
| Section 1: bootstrap attributed to Efron 1979 | Original paper's first-page bibliographic information and DOI metadata agree. [Original paper](https://blogs.helsinki.fi/bk-club/files/2012/05/Efron_Bootstrap_AS1979.pdf). |
| Section 2: plug-in principle and separate within-arm draws | Supported by the [Hesterberg accepted manuscript](https://arvindvenkatadri.com/teaching/3-order-and-chaos/modules/6b-mangoes/hesterberg2015.pdf), Sections 1.2–1.3 and 2, and [boot documentation](https://stat.ethz.ch/R-manual/R-devel/library/boot/html/boot.html). |
| Bootstrap SE as SD of replicates; percentile CI as quantiles | Verified against the definitions and implementation. Finite simulation approximates the exhaustive distribution. |
| Figure 1 draw counts, mean markers, histogram, buttons and readout | Executed initial, one, two, additional 100, additional 1,000, ideal and reset states. Default readout matches the numerical evidence. |
| Maximum difference 30; 10^10 ordered draws per arm | Directly checked: 21 − (−9) = 30; 10 choices in each of 10 draws gives 10^10, including distinct participants with the same recorded value. |
| Exact convolution, centre 7.5, SE 3.16, percentile 1.3–13.7 | Independent integer-count convolution totals 10^20 joint ordered draws. Mean 7.5, SD 3.158006, endpoints 1.3 and 13.7. JS probability distributions sum to one within floating-point precision. |
| Bootstrap versus permutation: replacement, arm separation and centre | Verified against both articles' data and implementations. The permutation interpretation is conditional on the appropriate null/assignment assumptions explained in the previous post. |
| Section 3: divisor n versus n−1; factor 0.949 | Direct variance derivation and recomputation give sqrt(9/10). Equal arm sizes justify the common factor here; unequal sizes require arm-specific contributions. |
| Section 3: normal-quantile versus t approximation | Correctly presented as an approximation for these data, not an exact normal identity for a discrete bootstrap distribution. |
| Width 12.4 versus about 14.0; ratio 0.885; about 11% narrower | Recalculated from unrounded t quantile and SE. Width ratio approximation 0.885033. |
| Ratios for 5, 10, 20, 40 per arm | Recomputed: 0.760209, 0.885033, 0.943658, 0.972103; reported rounding agrees. |
| Section 4: several CI methods and boot implementation | [boot.ci documentation](https://stat.ethz.ch/R-manual/R-devel/library/boot/html/boot.ci.html) lists percentile, BCa and studentized intervals and the required variance estimates. |
| BCa publication, bias correction, acceleration and no narrowness correction | Supported by DOI metadata, the original Efron paper and Hesterberg's extended discussion. Latest acceleration wording is more precise; exports are stale (F1). |
| Exact BCa endpoints for both datasets | Independent calculation with strict “below estimate” bias correction: 1.3–13.7 and 2.8–21.5. The JS acceleration and adjusted quantiles agree. |
| Bootstrap-t statistic and inversion | Verified: resampled centred difference divided by resampled SE; invert with the observed SE and reversed tail quantiles. |
| Table 2: Student and Welch endpoints, both datasets | SciPy and the published R example agree after rounding. Outlier Student limits −0.181751–19.981751; Welch −0.410830–20.210830. |
| Table 2: inverted permutation interval | Enumerated all 184,756 assignments and checked boundaries. Acceptance-set limits approximately 0.5–14.5 and 0.6–20.0. Constant-shift assumption is explicit. |
| Table 2: bootstrap-t 0.5–14.6 and 1.7–23.7 | Fresh 10-million-draw runs give 0.544–14.634 and 1.731–23.722; reported rounding agrees. These are simulation estimates, not exact endpoints. |
| Figure 2: t curve, SEs, mean/median switches and intervals | Executed all dataset/statistic combinations. Curve is expressly distinguished from the normal sampling distribution of the raw estimator. |
| Outlier example: 35%, 39%, 26% and about 3.7 per copy | Binomial probabilities 0.348678, 0.387420, 0.263901. Expected conditional increment `(45 − mean(other nine))/10 = 3.688889`. Each individual draw need not contribute exactly that amount. |
| Median: 5th/6th order statistics, 85 values, mode 5.0 at 4.5% | Independent exact multinomial-count calculation confirms 85 possible differences and mode probability 0.04495354 for Table 1. |
| Median percentile −2.5–15.5 in both datasets | Confirmed by exact enumeration. Moving the maximum does change the entire bootstrap median distribution (126 possible differences in the outlier dataset); the two reported quantiles remain unchanged. |
| Median performance caveat | Supported by Hesterberg's discussion; current source also qualifies that percentile intervals can be reasonable. That qualification is missing from exports (F1). |
| Figure 3: 1,000 trials, 999 resamples, true difference 8, SD 8, selectable designs | Checked source algorithm and all desktop combinations of population, size and displayed method. |
| Figure 3 default: four misses in first 100; coverages 94.4%, 90.6%, 90.4%, 95.1% | Fresh browser execution reproduces the exported figure's aria/readout values exactly. |
| Table 3: distribution, log-scale sigma 1, skewness about 6 | Recomputed lognormal mean/variance standardization; skewness 6.184877. Shift equivariance justifies using zero true difference for the table. |
| Table 3: all coverage cells and software/seeds | Reran four seeds × 2,500 trials with 1,999 resamples for each population/size; all cells match at integer-percent rounding. Python 3.9.6, NumPy 2.0.2 and SciPy 1.13.1 match the stated versions. |
| Table 3: Monte Carlo SE about 0.2/0.4 percentage points | Binomial formula gives 0.217945 at coverage .95 and 0.357071 at .85. |
| Normal/skewed coverage narrative and mean widths | Fresh totals reproduce widths 25.7509 vs 22.4896, and 34.2468 vs 18.2651. Scenario qualifiers are necessary and present. |
| Equal-shape equal-size difference symmetry and zero population BCa terms | Direct proof: swapping two independent identically distributed centred arm means changes the sign but not the distribution. Signed third influence moments cancel. This does not extend to unequal arm distributions/sizes. |
| Further 3,000-trial BCa check | Fresh seed-5 rerun: at n=10, percentile/BC/BCa 89.5/88.3/85.0%; at n=20, 91.9/90.4/86.7%. Drops support the approximate stated ranges. |
| Section 6: no normal assumption; sample as population proxy | Valid description of the ordinary nonparametric procedure, with dependence qualification F2 and method-specific validity qualification F5. |
| Table 4: independent groups, strata, pairs, clusters and repeated participants | Appropriate starting rules for those settings. In a stratified trial, preserve relevant arm-by-stratum counts when conditioning on both; a complex sampling design may need weights or a specialized bootstrap. The table is explicitly a starting point. |
| Table 4: time series | Blocks are appropriate for suitable dependence conditions; the unqualified independence statement is F2. Original cited full text not directly inspected; see access limitations below. |
| Table 4: regression | Latest source includes fixed-design/conditioning rationale, rare-category warning, model fit and constant-variance requirements. Supported by Hesterberg Section 5.1. Missing qualifications in exports are F1, not a reopened HTML defect. |
| Table 4 and checklist: repeat adaptive steps | Correct for targeting the whole procedure's variability, but not sufficient to establish validity of post-selection CIs (F5). |
| Table 5: every displayed central range | Seed-12 rerun reproduces all reported values; F4 concerns documentation and precision interpretation. |
| Section 7: 10,000 routine resamples and 15,000 criterion | Hesterberg Section 3.3 supports both. The latter is a criterion about tail-probability Monte Carlo precision, not a guarantee of adequate sample information or CI coverage. |
| Section 8: reporting checklist and sentences | Appropriate description of the statistic, resampling, CI method, draws, versions and seed. R results sentence agrees with execution. |
| Published R code and comments | Extracted and executed unchanged using R 4.5.2, boot 1.3-32: SE 3.113078; percentile 1.5–13.6; studentized .594–14.414; pooled t .506387–14.493613. |
| Traps 9.1 and 9.4 | Numerical cross-references checked against tables and execution. The small-sample caution is appropriately scoped to percentile intervals in these examples. |
| Traps 9.2 and 9.3 | Correct unit/procedure advice; absolute direction of error requires F3, and post-selection validity needs F5. |
| Trap 9.5: centring and bootstrap bias | Difference-in-means centring proved and checked exactly. For the median example the exhaustive mean differs from the observed median difference, illustrating the stated distinction. |
| Bibliography and internal references | DOI identities, authors, publication years and available journal/page metadata checked. The 189–228 span for DiCiccio/Efron includes discussion/rejoinder; primary article alone is 189–212. No correction needed if the reference denotes the whole discussion. |

## Fresh coverage results

Values are percentages, before rounding to the article's integer percentages. See `evidence/coverage-summary.json` for full widths and counts.

| Population | Per arm | Student t | Percentile | BCa | Bootstrap-t |
|---|---:|---:|---:|---:|---:|
| Normal | 5 | 95.15 | 87.71 | 88.12 | 95.69 |
| Normal | 10 | 94.92 | 91.95 | 91.73 | 94.99 |
| Normal | 20 | 95.39 | 93.84 | 93.83 | 95.32 |
| Normal | 40 | 95.01 | 94.31 | 94.40 | 95.04 |
| Lognormal | 5 | 96.87 | 86.72 | 83.11 | 97.01 |
| Lognormal | 10 | 96.35 | 90.16 | 84.82 | 92.49 |
| Lognormal | 20 | 96.37 | 92.05 | 87.46 | 91.25 |
| Lognormal | 40 | 95.53 | 92.85 | 88.79 | 91.06 |

## Verification rounds and corrections to the audit

1. **Evidence round:** read the complete article text and scripts, re-executed the R example, exact convolution, exact median enumeration, permutation inversion, large bootstrap-t run, coverage simulations, Monte Carlo ranges and BCa diagnostic. Checked primary papers/documentation and bibliographic metadata. Preserved fresh outputs.
2. **Independent challenge round:** tested covariance and dependence counterexamples, distinguished source HTML from exported content, checked model-specific requirements, discreteness/ties and simulation-versus-exact precision. Executed interactive states and the offline-copy failure path. Compared JS probability/moment calculations to independent integer/rational Python computations. Corrected the audit's preliminary assumption that the regression caveat was absent from the latest HTML: it is absent only from exports. An automated text-box overlap flag in Figure 2 was rejected after inspecting actual glyph rendering; it is not a visual defect.
3. **Final full-scope round:** rechecked the complete ledger against the current source, verified report numbers against saved fresh results, checked quotations against HTML, verified all recorded input hashes remained unchanged, and challenged each finding's scope/severity. No new findings in this reviewed scope after the corrections to the audit. The five consolidated findings remain open in the article; this is not a claim that they were fixed.

The PDF was inspected as text and as page montages across all pages. Figures and tables were readable in the inspected renderings. Browser checks found no script errors or page-level horizontal overflow at the inspected desktop/mobile widths. This is limited rendering evidence, not a claim that all browsers, font-loading situations or assistive technologies were tested.

## Access limits and unverified items

- Künsch's original full text and Davison/Hinkley's full book were not accessible. Bibliographic identities were verified; the relevant general techniques were cross-checked with accessible primary research or official package documentation. Their complete texts were **not verified**.
- The original 1987 Efron PDF was accessible as a scan, but a full independent line-by-line transcription was not performed. Method formulas were cross-checked through the package documentation, Hesterberg and execution.
- Published historical claims were checked against primary records, not treated as evidence that no precursor existed.
- Exact ideal bootstrap-t quantiles were **not verified by exhaustive enumeration**. The reported rounded values are supported by the fresh 10-million-draw simulation. The empirical Table 5 central ranges are not mathematically exact 95% bounds.
- This review covers local files. Public GitHub Pages deployment equivalence, live comments, translation services, and every page of each linked earlier article were **not verified**.

## Reproducing the numerical checks

Run from the repository root. Scripts recovered from this project's earlier temporary calculation directory are retained here rather than relying on those temporary files. `monte_carlo.R` replaces slow columnwise variance calls with the algebraically equivalent sum-of-squares calculation; it preserves draw order and seed.

```sh
Rscript audits/bootstrap-2026-10-09/evidence/example.R
python3 audits/bootstrap-2026-10-09/evidence/exact.py
python3 audits/bootstrap-2026-10-09/evidence/median.py
python3 audits/bootstrap-2026-10-09/evidence/permutation.py
python3 audits/bootstrap-2026-10-09/evidence/bootstrap_t.py
python3 audits/bootstrap-2026-10-09/evidence/bca_diagnostic.py
Rscript audits/bootstrap-2026-10-09/evidence/monte_carlo.R
```

For each population (`normal`, `lognorm`), run `coverage.py POP SEED 2500` for seeds 11, 22, 33 and 44. Sum the hit and width counts by population/arm size and divide by 10,000. The stored JSONL files and `coverage-summary.json` contain the fresh outputs. `browser.cjs` and `second_round.cjs` use the local bundled Playwright and installed Chrome; their paths may need adapting on another computer.
