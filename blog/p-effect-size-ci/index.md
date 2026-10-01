# The p-value, the effect size and the confidence interval

*What each tells the reader, and how to report them in a paper*

Statistics note · Reporting in biomedical research

> Source: https://selcukorkmaz.github.io/blog/p-effect-size-ci/ · 1 October 2026

Selçuk Korkmaz\
1 October 2026

## In short

A *p*-value, an effect size and a confidence interval answer three different questions about the same result. The *p*-value asks how surprising the data would be if a specified hypothesis, usually "no difference", were true. The effect size asks how large the difference or association is. The confidence interval asks which sizes the data leave compatible, and so how precisely the study measured it. Only the second and third can tell a reader whether a finding matters, and the 95% interval also shows whether *p* is below 0.05 for the matching test.

The rule for papers follows from that. Lead with the effect estimate in its original units and its 95% confidence interval, add an exact *p*-value if you want one, and read the interval against the smallest effect that would matter. Three figures (two of them interactive) show how the three numbers behave, Table 4 words six typical patterns, and Table 5 and Table 6 show what to write and what to report for common analyses.

Keywords: *p*-values · effect size · confidence intervals · clinical significance · statistical reporting · reporting guidelines

## 1 Three numbers, three questions

Suppose a trial randomises 130 adults, 65 to a lifestyle programme and 65 to usual care, and measures systolic blood pressure after 12 weeks. The standard deviation (SD) is about 16 mmHg in both arms, and the programme arm ends up 6.2 mmHg lower. The results section could summarise this one finding with three numbers, and each answers a different question (Table 1).

**Table 1.** Three summaries of one result: a 6.2 mmHg lower blood pressure with the programme (65 per arm, SD 16 mmHg).

| Quantity | The question it answers | In the example | With more participants |
|----|----|----|----|
| **Effect size** | How large is the difference? | 6.2 mmHg (standardised: Hedges' *g* = 0.39, see Section 3) | Settles near the true value |
| **95% confidence interval (CI)** | Which sizes are compatible with the data, and how precisely was the effect measured? | 0.6 to 11.8 mmHg | Width shrinks in proportion to 1/√*n* |
| ***p*-value** | How surprising would a difference this far from zero be if the true difference were exactly zero? | *p* = 0.03 | Tends to fall, whatever the size of the effect, provided it is not exactly zero |

The three are not independent. The *p*-value and the interval are both built from the same two ingredients, the estimate (which is the effect size) and its standard error (SE), which I described in an [earlier note on the SD and the SE](https://selcukorkmaz.github.io/blog/sd-or-se/). For a difference in two means:

*D* = *x̄*<sub>1</sub> − *x̄*<sub>2</sub>

SE(*D*) = √\[*s*<sub>1</sub><sup>2</sup>/*n*<sub>1</sub> + *s*<sub>2</sub><sup>2</sup>/*n*<sub>2</sub>\]

95% CI = *D* ± *t*<sub>0.975</sub> × SE(*D*)

*p* = 2 × Pr(*T* ≥ \|*D* / SE(*D*)\|)

Here group 1 is usual care and group 2 the programme, each with mean *x̄*, SD *s* and size *n*, so *D* is usual care minus programme (positive values favour the programme); *t*<sub>0.975</sub> is the 97.5th percentile of the *t* distribution with the test's degrees of freedom, and *T* follows that distribution. In the example, SE = 16 × √\[2/65\] = 2.81 mmHg. The test statistic is 6.2 / 2.81 = 2.21 on 128 degrees of freedom, which gives *p* = 0.03, and with *t*<sub>0.975</sub> = 1.98 the 95% CI is 6.2 ± 1.98 × 2.81, or 0.6 to 11.8 mmHg.

Because the ingredients are shared, a two-sided *p*-value below 0.05 and a 95% confidence interval that excludes zero are the same statement, when both are computed from the same test statistic and standard error, as with the *t*-test and *t*-interval here. (For proportions, a Wald interval and a pooled test can disagree near the boundary.) So the interval already tells the reader whether *p* is below 0.05, and it adds the size and precision that the *p*-value hides. Gardner and Altman recommended reporting both, and dropping the *p*-value first if one had to be omitted \[1\].

## 2 The *p*-value

A *p*-value is the probability of getting a test statistic at least as extreme as the one observed, computed on the assumption that the null hypothesis and every other assumption of the statistical model are true \[2\]. In the example, *p* = 0.03 says that if the programme had no effect at all and the model were right, a difference of 6.2 mmHg or more in either direction would turn up about 3 times in 100 repetitions of the trial.

Greenland and colleagues describe it as a continuous measure of compatibility between the data and the whole set of assumptions used to compute it: a small value signals that something in that set, the null hypothesis or another assumption, is doubtful \[2\]. Rafi and Greenland add a way to feel its size: the surprisal, or S-value, *S* = −log<sub>2</sub>(*p*), in bits (written *S* here to keep it apart from the SD *s*). A *p* of 0.03 is about 5 bits, as surprising as five heads in a row from a fair coin \[3\].

**What a *p*-value does not do.** It is not the probability that the null hypothesis is true, or that the data arose by chance alone. It does not measure the size of an effect or the importance of a result. By itself it is not a good measure of evidence about a model or hypothesis. And a conclusion should not be based only on whether it falls on one side of a threshold \[4\].

The most useful thing to know about a *p*-value is that it depends on the sample size as much as on the effect. Figure 1 holds the SD at 16 mmHg and changes the group size. In one view the observed difference stays at 5 mmHg, and *p* nevertheless runs from 0.49 to below 0.001. In the other, every row is chosen so that *p* = 0.03, and the estimate runs from 16.9 mmHg down to 0.9.

![Six rows of 95% confidence intervals for the difference in blood pressure between two groups, at 10 to 3,000 participants per group. With the estimate held at 5 mmHg, the p-value falls from 0.49 to below 0.001 as the intervals narrow.](https://selcukorkmaz.github.io/blog/p-effect-size-ci/fig1.svg)

**Figure 1. The same effect can have any *p*-value, and the same *p*-value any effect.** Two-arm comparison of systolic blood pressure with an SD of 16 mmHg in each arm. Each row shows the difference in means (positive favours the programme) with its 95% CI, the two-sample *t*-test *p*-value and Hedges' *g*. Effect fixed: the difference is 5 mmHg at every group size, so *p* falls and the interval narrows as the groups grow. *p* fixed: each row is chosen so that *p* = 0.03, so the estimate shrinks as the groups grow. The dashed line marks 5 mmHg, assumed here to be the smallest difference of interest. On the interactive page the buttons switch between the two views; the static copy shows the first. With *p* fixed, the estimates are 16.9, 9.2, 4.9, 2.8, 1.6 and 0.9 mmHg.

Two consequences follow. A *p*-value below 0.05 says the data are hard to reconcile with an effect of exactly zero. It does not say the effect is big enough to matter, and in a large enough study a difference of 0.9 mmHg will reach it. A *p*-value above 0.05 does not say there is no effect either; it may only mean the study was small \[2\].

## 3 The effect size

An effect size is how large the difference or association is. It answers the question the reader actually has: how much? It can be *unstandardised*, in the units of the outcome (6.2 mmHg, 2 days, 8 percentage points), or *standardised*, expressed in units of variability or as a ratio, so that it has no units (Table 2).

Prefer the unstandardised form whenever the units mean something to your readers, because they can judge it directly against what they know about blood pressure, length of stay or risk \[5,6\]. Use a standardised effect size when the outcome has no intrinsic units \[6\], when studies used different scales to measure the same construct \[5,6\], or when you need to compare or pool results across studies \[6\], and give its confidence interval as well. Standardising an arbitrary or poorly measured scale obscures its deficiencies rather than fixing them \[5\].

**Table 2.** Common effect sizes by type of outcome.

| Outcome and comparison | Unstandardised | Standardised or relative |
|----|----|----|
| Continuous, two groups | difference in means (with units) | Cohen's *d*, Hedges' *g* |
| Continuous, paired or repeated | mean of the paired differences | standardised mean change (state the SD used) |
| Binary outcome | risk difference (percentage points), number needed to treat | risk ratio, odds ratio |
| Time to event | difference in median or restricted mean survival time | hazard ratio |
| Two continuous variables | regression slope (outcome units per unit of exposure) | correlation coefficient *r* |
| Three or more groups, or a model | contrasts between group means | *η*<sup>2</sup>, partial *η*<sup>2</sup>, *R*<sup>2</sup> (shares of variance explained) |
| Ranks or ordinal data | Hodges–Lehmann shift, with each group's median and interquartile range (IQR) | probability of superiority |

The best-known standardised measure for two means is Cohen's *d*, the difference divided by the pooled SD. Hedges' *g* multiplies it by a small correction, which matters when the groups are small \[7,8\]. An approximate SE for *g* gives its confidence interval \[8\]:

*d* = *D* / *s*<sub>pooled</sub>

*g* ≈ *d* × \[1 − 3 / (4(*n*<sub>1</sub> + *n*<sub>2</sub>) − 9)\]

SE(*g*) ≈ √\[(*n*<sub>1</sub> + *n*<sub>2</sub>) / (*n*<sub>1</sub>*n*<sub>2</sub>) + *g*<sup>2</sup> / (2(*n*<sub>1</sub> + *n*<sub>2</sub>))\]

In the example, *d* = 6.2 / 16 = 0.39, *g* = 0.39 and its 95% CI, *g* ± 1.96 × SE(*g*) with SE(*g*) = 0.177, is 0.04 to 0.73. A standardised effect is only as interpretable as its denominator: *d* shrinks if the sample is more heterogeneous, even when the raw effect is unchanged \[5\]. State which SD was used.

### 3.1 What counts as large?

Cohen's conventions are 0.2, 0.5 and 0.8 for *d* (small, medium, large), with matching values for other measures (Table 3) \[9\]. Cohen presented them as reference points to use only when nothing better is available \[7,9\]. Something better is almost always available: the smallest effect that would matter to patients, clinicians or the science. The Statistical Analyses and Methods in the Published Literature (SAMPL) guidelines ask authors, where possible, to say what minimum difference they consider clinically important, and not to call a correlation low, moderate or high unless they define the ranges \[10\]. For patient outcomes, that threshold is often called the minimal clinically important difference, which was originally defined as the smallest difference in the domain of interest that patients perceive as beneficial and that would mandate a change in management, in the absence of troublesome side effects and excessive cost \[11\]. It is the yardstick for reading an interval in Section 5.

**Table 3.** Cohen's conventions for three common measures. Use them only as a last resort, and prefer a threshold based on your field and your outcome.

| Measure                             | Small | Medium | Large |
|-------------------------------------|-------|--------|-------|
| Difference between two means, *d*   | 0.2   | 0.5    | 0.8   |
| Correlation, *r*                    | 0.1   | 0.3    | 0.5   |
| Variance explained, *η*<sup>2</sup> | 0.01  | 0.06   | 0.14  |

## 4 The confidence interval

A 95% confidence interval is the range of values produced by a procedure that, across repeated studies and if the model's assumptions hold, would contain the true value in 95% of them \[2\]. That statement is about the procedure, not about the one interval in front of you. The reading that works in practice is the one Rafi and Greenland propose: an interval shows the values most compatible with the data under the model, with the estimate in the middle the most compatible, and values near the ends less so \[3\]. The usual shortcut, "there is a 95% probability that the true value lies in this interval", is not what the interval means, and it is one of the misreadings that researchers commonly endorse \[12\].

Figure 2 shows how the interval, the estimate and the *p*-value fit together. Take every possible true difference in turn and ask how compatible the data are with it, using the same *t*-test that gave the *p*-value for zero. The result is a curve, the *p*-value function. Its peak is the estimate. The *p*-value reported for "no difference" is only the height of the curve at zero. And the 95% confidence interval is the stretch of the horizontal axis where the curve lies above 0.05 \[3\]. The curve is not a probability distribution for the true difference \[3\]: its height is the two-sided *p*-value of each hypothesis. It equals exactly 1 at the estimate, where the test statistic is 0, and it has a sharp point there because the *p*-value ignores the sign of the difference.

![The p-value function for an observed difference of 6.2 mmHg: a curve peaking at the estimate, with the p-value for zero read off at zero and the 95% confidence interval where the curve lies above 0.05.](https://selcukorkmaz.github.io/blog/p-effect-size-ci/fig2.svg)

**Figure 2. One curve holds the estimate, the *p*-value and the interval.** Observed difference 6.2 mmHg, SD 16 mmHg in each arm. For each hypothesised true reduction on the horizontal axis, the curve gives the two-sided *p*-value of the *t*-test of that hypothesis. The peak is the estimate; the *p*-value reported in a paper is the height of the curve at 0; the confidence interval is the part of the axis where the curve lies above the dashed line at *α* = 1 − confidence level. More participants make the curve narrower, so the interval shrinks and the *p*-value at 0 falls while the peak stays where it is. The curve is not a probability distribution for the true difference.

Three practical points follow from the picture.

- **Width is precision.** The interval's width shrinks in proportion to 1/√*n*, so four times as many participants roughly halve it, and a wide interval says the study cannot pin the effect down, whatever its *p*-value.
- **Ratio intervals are symmetric on the log scale.** Intervals for risk ratios, odds ratios and hazard ratios are usually calculated on the log scale, so they are not centred on the estimate, and the no-effect value is 1, not 0.
- **An interval is only as good as its assumptions.** It reflects sampling variation only \[1\]; it does not correct for bias, and it is a best-case measure of uncertainty because it depends on the model being right \[2\]. A narrow interval around a biased estimate is a precise wrong answer. And intervals of two separate groups say little about their difference \[2\]; estimate the difference itself, as the [note on error bars](https://selcukorkmaz.github.io/blog/sd-or-se/#bars) shows.

Gardner and Altman argued in 1986 that confidence intervals should be used for the major findings, in the main text and in the abstract \[1\]. Current guidelines, discussed in Section 6, ask for the same estimate-plus-interval reporting \[10,13,14\].

## 5 Reading the three together

**Compare the interval with two reference points.** Zero, or one for a ratio, tells you whether the data are compatible with no effect. The smallest effect of interest tells you whether the compatible values would matter. Where the interval sits relative to both gives the interpretation.

Figure 3 places six illustrative intervals against a zone of trivial effects (here ±5 mmHg). The first three are statistically significant, and the last three are not, yet within each group the meaning differs a great deal (Table 4).

![Six 95% confidence intervals for a reduction in blood pressure, drawn against a shaded zone of trivial effects from minus 5 to 5 mmHg. Three exclude zero and three include it, with different meanings.](https://selcukorkmaz.github.io/blog/p-effect-size-ci/fig3.svg)

**Figure 3. Six ways an interval can sit relative to zero and to the smallest effect of interest.** Illustrative 95% confidence intervals (dots are the estimates) for the reduction in systolic blood pressure with a programme; positive values favour the programme. The shaded zone covers differences of 5 mmHg or less in either direction, assumed here to be too small to matter. *p*-values come from a normal approximation to each interval. Rows 1 to 3 are statistically significant and rows 4 to 6 are not.

**Table 4.** Wording for each pattern in Figure 3.

| Pattern | What the data support | Wording |
|----|----|----|
| 1\. Significant, clearly important | Incompatible with no effect, and every compatible value is important | "Blood pressure was 12 mmHg lower (95% CI 7 to 17), more than the 5 mmHg we regarded as important." |
| 2\. Significant, importance unclear | Incompatible with no effect, but compatible values run from trivial to important | "Blood pressure was 6 mmHg lower (95% CI 1 to 11). The data are incompatible with no effect but cannot say whether the benefit exceeds 5 mmHg." |
| 3\. Significant, too small to matter | Incompatible with no effect, but no compatible value is important | "Blood pressure was 2.3 mmHg lower (95% CI 0.5 to 4.1); every compatible value is below the 5 mmHg we regarded as important." |
| 4\. Not significant, inconclusive | Compatible with no effect and with a large benefit | "Blood pressure was 7 mmHg lower (95% CI 1 higher to 15 lower; *p* = 0.09). The data are compatible with no effect and with a benefit well above 5 mmHg." |
| 5\. Not significant, inconclusive | Compatible with a harm and with a benefit that both exceed 5 mmHg | "Blood pressure was 1.5 mmHg higher (95% CI 9.0 higher to 6.0 lower). The study is too imprecise to say whether the programme helps or harms, or by how much." |
| 6\. Not significant, no important effect | Compatible only with trivial differences in either direction | "Blood pressure was 0.5 mmHg lower (95% CI 2.5 higher to 3.5 lower). The data are compatible only with differences smaller than 5 mmHg in either direction." (Only if the margin was set in advance.) |

Rows 4 and 5 show why "not significant" must never be read as "no effect". The mistake is common: in a compilation of four published surveys covering 791 articles in five journals, Amrhein and colleagues reported that about half (402, or 51%) wrongly read a non-significant result as showing no effect \[15\]. As Altman and Bland put it, absence of evidence is not evidence of absence \[16\]. To claim that an effect is negligible, as in row 6, you need a confidence interval that lies inside a margin based on the smallest effect of interest, which is the logic of equivalence testing \[17\]. Set the margin before seeing the data. The usual two one-sided tests at the 5% level correspond to a 90% interval, and a 95% interval is more demanding \[17\]. SAMPL asks authors to report the equivalence margin \[10\].

## 6 How to report them in a paper

**Rule of thumb.** Estimate first, interval second, *p*-value last and optional, everything in the units of the outcome, and a sentence that says what the interval means against the smallest effect of interest.

Reporting guidelines agree. The SAMPL guidelines ask authors to give the estimate, or effect size, with a measure of precision, usually a 95% confidence interval, and not to rely on *p*-values alone \[10\]. The Consolidated Standards of Reporting Trials (CONSORT) 2025 statement, item 26, asks trial reports to give, for each primary and secondary outcome, the estimated effect size and its precision, such as a 95% CI, and for binary outcomes both the absolute and the relative effect \[13,18\]. The International Committee of Medical Journal Editors (ICMJE) recommendations ask for appropriate measures of uncertainty, such as confidence intervals, rather than reliance on hypothesis tests alone \[14\].

### 6.1 The basic sentence

Table 5 shows one result written three ways. The weak version hides the size and the precision; the better one gives the size but not the precision; the best gives both and reads them against the smallest effect of interest.

**Table 5.** One result, three ways of reporting it.

| Version | Text | What is missing |
|----|----|----|
| Weak | "The programme significantly reduced blood pressure (*p* \< 0.05)." | Size, precision, exact *p*, the comparison, the units |
| Better | "Blood pressure fell 6.2 mmHg more with the programme (*p* = 0.03)." | Precision: the reader cannot tell a benefit of about 1 mmHg from one of about 12 |
| Best | "At 12 weeks, mean systolic blood pressure was 6.2 mmHg lower in the programme group (*n* = 65) than in the usual-care group (*n* = 65) (95% CI 0.6 to 11.8; *p* = 0.03; Hedges' *g* = 0.39, 95% CI 0.04 to 0.73). The interval includes differences below the 5 mmHg named in the protocol as the smallest effect of interest, so the data are incompatible with no benefit but do not establish that the benefit is important." | Nothing essential |

### 6.2 Formatting rules

- **Say what the difference is.** Name the direction (for example usual care minus programme, or "lower in the programme group"), the units and the confidence level (95% CI).
- **Write intervals with "to".** "−3.9 to 6.3" is unambiguous with negative numbers, where a dash is not. Give the estimate and both limits the same number of decimals, and no more precision than the data support.
- **Give exact *p*-values.** Write *p* = 0.03, not *p* \< 0.05, and never "NS". SAMPL calls *p*-values less preferred than confidence intervals but, if they are given, asks for equalities to one or two decimals, with *p* \< 0.001 as the smallest value worth reporting \[10\]. My own habit is two decimals, three below 0.01 or when the value is close to 0.05 (so 0.049 is not rounded to 0.05). Never write *p* = 0.000.
- **Name the test and the sidedness** in the methods, and say whether tests were two-sided and what *α* was, if you use a threshold at all \[10\].
- **Do not use stars alone.** Asterisks in a table are no substitute for the estimate and the interval.
- **Define the standardised effect size.** Say whether *d* or *g*, which SD was used \[7\], which group was subtracted from which, and give its 95% CI.
- **Take a position on "significant".** Some statisticians recommend dropping the phrase "statistically significant" altogether \[15,19\], and journals differ. If you use it, define *α* in advance and never let it stand in for the estimate.

### 6.3 Binary outcomes: report both scales

For a binary outcome, give the absolute effect (risk difference) and the relative effect (risk ratio or odds ratio), each with its interval \[13\]; the number needed to treat (NNT) can also help \[13\]. A relative effect alone can make a rare outcome look important, and an absolute effect alone hides how it scales with baseline risk \[13\]. With 18 events among 200 participants in one arm and 34 among 200 in the other:

Events occurred in 18 of 200 participants (9.0%) in the intervention group and 34 of 200 (17.0%) in the control group: risk difference −8.0 percentage points (intervention minus control; 95% CI −14.5 to −1.5; *p* = 0.02); risk ratio 0.53 (95% CI 0.31 to 0.91). The number needed to treat to prevent one event was 13 (95% CI 7 to 69).

The interval for the NNT comes from inverting the unrounded limits of the risk difference. That is straightforward only when the risk-difference interval excludes zero, as it does here; when it does not, the interval for the NNT is not a single range, and Altman shows how to report it \[20\].

### 6.4 Non-significant results

Report them exactly like significant ones, with the estimate, the interval and the exact *p*-value, and describe what the interval rules out:

Mean systolic blood pressure was 1.2 mmHg lower in the programme group (95% CI 3.9 higher to 6.3 lower; *p* = 0.64). The data are compatible with a reduction larger than the 5 mmHg we set as the smallest effect of interest and with a modest increase, so the trial is inconclusive rather than negative.

### 6.5 Tables, figures and the abstract

In a table, give one column for the estimate with its interval and, if wanted, one for the *p*-value; state in the footnote what the estimate is, what test gave the *p*-value, and whether tests were adjusted for multiplicity. For many outcomes or subgroups, a forest plot with the reference line at no effect and a second line at the smallest effect of interest lets readers do Section 5 for themselves. The abstract should carry the estimate and 95% interval of the primary outcome, not just a *p*-value \[1\]. Table 6 lists what to report for common analyses.

**Table 6.** What to report for common analyses.

| Analysis | Effect estimate | Interval | Also useful |
|----|----|----|----|
| Two independent means | difference in means (A − B), with units | Welch 95% CI | Hedges' *g* with CI if the scale is arbitrary; *n*, mean and SD per group |
| Paired or repeated measures | mean of the paired differences | 95% CI of that mean | the SD of the differences |
| Two proportions | risk difference and risk ratio | 95% CI for each | number needed to treat with its interval; if the risk-difference interval includes 0, report it as described by Altman \[20\] |
| Logistic regression | odds ratio | 95% CI | absolute risks at chosen covariate values |
| Linear regression | coefficient, in outcome units per unit of the predictor | 95% CI | the unit of the predictor stated explicitly |
| Time to event | hazard ratio | 95% CI | median survival or restricted mean difference, with CI |
| Correlation | *r* (or *ρ*) | 95% CI | scatter plot; no "low", "moderate" or "high" without stated ranges \[10\] |
| Three or more groups | pairwise differences or planned contrasts | 95% CIs (adjusted if several) | the omnibus test and partial *η*<sup>2</sup>, with CI |
| Rank-based comparison | Hodges–Lehmann shift or probability of superiority | 95% CI | median (IQR) in each group |

### 6.6 Sentences to adapt

- **Methods.** "The primary outcome was the between-group difference in systolic blood pressure at 12 weeks, estimated with Welch's *t*-test. Tests were two-sided with *α* = 0.05, and results are reported as differences with 95% confidence intervals and exact *p*-values. The smallest effect of interest, 5 mmHg, was specified before data collection. No adjustment was made for secondary outcomes, which are exploratory."
- **Table footnote.** "Estimates are differences in means (usual care − programme; positive values favour the programme) with 95% CI from Welch's *t*-test; *p*, two-sided, unadjusted."
- **Figure legend.** "Squares show the reduction in systolic blood pressure (usual care − programme; positive values favour the programme) and horizontal lines show 95% confidence intervals. The dashed line marks the smallest effect of interest (5 mmHg)."

Base R gives the estimate, interval and *p*-value for a two-group comparison of means or proportions; the risk ratio and the NNT above are computed by hand from the counts. The `effectsize` package adds the standardised effect with its interval; check that its sign convention matches the direction you report. Its interval is the exact (noncentral *t*) one, so it can differ slightly from the approximation above.

``` r
d$arm <- factor(d$arm, levels = c("usual care", "programme"))   # first − second
fit <- t.test(sbp ~ arm, data = d)              # Welch test
unname(fit$estimate[1] - fit$estimate[2])       # usual care − programme
fit$conf.int                                    # its 95% CI
fit$p.value                                     # two-sided p
effectsize::hedges_g(sbp ~ arm, data = d)       # Hedges' g with 95% CI

# Wald CI and pooled-test p; sign is intervention − control
prop.test(c(18, 34), c(200, 200), correct = FALSE)
```

## 7 Five traps

### 7.1 Treating 0.05 as a cliff

A result with *p* = 0.049 and one with *p* = 0.051 are practically the same evidence, and no sensible reading treats them as opposites. Phrases such as "a trend towards significance" for 0.06, or "highly significant" for 0.001, treat the threshold as if it were a fact about the world. Report the number and let readers weigh it. The American Statistical Association's statement says that conclusions should not be based only on whether a *p*-value passes a threshold \[4\].

### 7.2 Reading "not significant" as "no effect"

Covered in Section 5: a wide interval that includes zero is not evidence of absence \[16\]. Read the whole interval, and reserve claims of no important effect for intervals inside a margin set in advance.

### 7.3 Comparing significance levels of two groups

The difference between "significant" and "not significant" is not itself statistically significant \[21\]. Suppose a treatment effect is 25 (SE 10) in one subgroup and 10 (SE 10) in another. The first is significant (*p* = 0.01) and the second is not (*p* = 0.32), but the difference between them is 15 with an SE of 14, and *p* = 0.29. To claim that subgroups differ, test the difference, with an interaction term, and report its interval.

### 7.4 Reporting observed power

Power calculated from the observed result is a direct function of the *p*-value and adds no information; a non-significant result always has observed power of about 50% or less \[22\]. Report the confidence interval instead, which shows what the study could and could not exclude. Power belongs in the planning of a study, computed for a difference you named in advance.

### 7.5 Uncounted tests

With 20 independent tests of true null hypotheses at *α* = 0.05, the chance of at least one *p* below 0.05 is 1 − 0.95<sup>20</sup> = 64%. Reporting only the significant ones, or presenting a chosen analysis as if it had been the plan, makes the *p*-values and the intervals misleading \[2\]. State which outcomes were primary and how multiplicity was handled \[10\].

## 8 A checklist for authors and reviewers

- Every main result gives the estimate in original units, its direction, and a 95% confidence interval.
- The comparison is stated (A − B, or "lower in group A"), and so is the confidence level.
- *p*-values are exact (*p* = 0.03; *p* \< 0.001 only below that), never "NS", never *p* = 0.000, and never stars alone.
- Standardised effect sizes are named and defined, come with a confidence interval, and are not judged by Cohen's labels alone.
- Binary outcomes give the absolute and the relative effect.
- The smallest effect of interest is stated in the methods, with how it was chosen, and the interval is read against it.
- Non-significant results are described by what their interval excludes, not as "no effect".
- The test, the sidedness, *α*, the primary outcome, and any adjustment for multiple comparisons are in the methods.
- The abstract has the estimate and interval of the primary outcome.

The *p*-value tells the reader whether zero is a comfortable value for the effect. The effect size tells them how large it is, and the interval how well the study knows it. Give them the last two first \[1\].

## References

1.  Gardner MJ, Altman DG. Confidence intervals rather than P values: estimation rather than hypothesis testing. *British Medical Journal (Clinical Research Ed)*. 1986;292(6522):746–750. doi:10.1136/bmj.292.6522.746
2.  Greenland S, Senn SJ, Rothman KJ, et al. Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations. *European Journal of Epidemiology*. 2016;31(4):337–350. doi:10.1007/s10654-016-0149-3
3.  Rafi Z, Greenland S. Semantic and cognitive tools to aid statistical science: replace confidence and significance by compatibility and surprise. *BMC Medical Research Methodology*. 2020;20:244. doi:10.1186/s12874-020-01105-9
4.  Wasserstein RL, Lazar NA. The ASA statement on *p*-values: context, process, and purpose. *The American Statistician*. 2016;70(2):129–133. doi:10.1080/00031305.2016.1154108
5.  Baguley T. Standardized or simple effect size: what should be reported? *British Journal of Psychology*. 2009;100(3):603–617. doi:10.1348/000712608X377117
6.  Sullivan GM, Feinn R. Using effect size—or why the P value is not enough. *Journal of Graduate Medical Education*. 2012;4(3):279–282. doi:10.4300/JGME-D-12-00156.1
7.  Lakens D. Calculating and reporting effect sizes to facilitate cumulative science: a practical primer for *t*-tests and ANOVAs. *Frontiers in Psychology*. 2013;4:863. doi:10.3389/fpsyg.2013.00863
8.  Hedges LV, Olkin I. *Statistical Methods for Meta-Analysis*. Academic Press; 1985.
9.  Cohen J. *Statistical Power Analysis for the Behavioral Sciences*. 2nd ed. Lawrence Erlbaum Associates; 1988.
10. Lang TA, Altman DG. Basic statistical reporting for articles published in biomedical journals: the "Statistical Analyses and Methods in the Published Literature" or the SAMPL Guidelines. *International Journal of Nursing Studies*. 2015;52(1):5–9. doi:10.1016/j.ijnurstu.2014.09.006. Full text: https://www.equator-network.org/wp-content/uploads/2013/07/SAMPL-Guidelines-6-27-13.pdf
11. Jaeschke R, Singer J, Guyatt GH. Measurement of health status: ascertaining the minimal clinically important difference. *Controlled Clinical Trials*. 1989;10(4):407–415. doi:10.1016/0197-2456(89)90005-6
12. Hoekstra R, Morey RD, Rouder JN, Wagenmakers EJ. Robust misinterpretation of confidence intervals. *Psychonomic Bulletin & Review*. 2014;21(5):1157–1164. doi:10.3758/s13423-013-0572-3
13. Hopewell S, Chan AW, Collins GS, et al. CONSORT 2025 explanation and elaboration: updated guideline for reporting randomised trials. *BMJ*. 2025;389:e081124. doi:10.1136/bmj-2024-081124
14. International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals: Preparing a Manuscript for Submission to a Medical Journal, Methods, Statistics. Updated January 2026. Available at https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html (accessed 1 October 2026).
15. Amrhein V, Greenland S, McShane B. Scientists rise up against statistical significance. *Nature*. 2019;567(7748):305–307. doi:10.1038/d41586-019-00857-9. The counts (402 of 791) are in the Supplementary Information.
16. Altman DG, Bland JM. Absence of evidence is not evidence of absence. *BMJ*. 1995;311(7003):485. doi:10.1136/bmj.311.7003.485
17. Lakens D. Equivalence tests: a practical primer for *t* tests, correlations, and meta-analyses. *Social Psychological and Personality Science*. 2017;8(4):355–362. doi:10.1177/1948550617697177
18. Hopewell S, Chan AW, Collins GS, et al. CONSORT 2025 statement: updated guideline for reporting randomised trials. *BMJ*. 2025;389:e081123. doi:10.1136/bmj-2024-081123
19. Wasserstein RL, Schirm AL, Lazar NA. Moving to a world beyond "*p* \< 0.05". *The American Statistician*. 2019;73(sup1):1–19. doi:10.1080/00031305.2019.1583913
20. Altman DG. Confidence intervals for the number needed to treat. *BMJ*. 1998;317(7168):1309–1312. doi:10.1136/bmj.317.7168.1309
21. Gelman A, Stern H. The difference between "significant" and "not significant" is not itself statistically significant. *The American Statistician*. 2006;60(4):328–331. doi:10.1198/000313006X152649
22. Hoenig JM, Heisey DM. The abuse of power: the pervasive fallacy of power calculations for data analysis. *The American Statistician*. 2001;55(1):19–24. doi:10.1198/000313001300339897
