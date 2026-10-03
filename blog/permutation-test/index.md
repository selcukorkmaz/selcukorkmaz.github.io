# Where a p-value comes from

*The permutation test, the null distribution and the distribution of the p-value itself*

Statistics note · Inference in biomedical research

> Source: https://selcukorkmaz.github.io/blog/permutation-test/ · 3 October 2026

Selçuk Korkmaz\
3 October 2026

## In short

Every *p*-value is a tail area of a null distribution: the distribution the test statistic would have if the null hypothesis, and the rest of the model, were true. Most tests take that distribution from a formula, such as the *t* distribution. A permutation test builds it from the data. If a treatment did nothing, the group labels in a randomised trial are arbitrary, so we can shuffle them, recompute the statistic each time, and count how often a shuffled result is at least as extreme as the real one. In a 20-person example, all 184,756 possible shuffles give *p* = 0.041 and the *t*-test gives *p* = 0.037: the *t* distribution is a smooth stand-in for the shuffle distribution.

Three interactive figures build the null distribution by shuffling, set it against the *t* distribution to show where the two part company, and show that the *p*-value itself has a distribution across repeated studies: flat when the null hypothesis is true, piled up near zero when it is not. Tables cover how many shuffles are enough, what a shuffle assumes, what to shuffle in each design and how shuffling differs from the bootstrap, and a checklist covers what to report.

Keywords: *p*-values · permutation tests · randomisation tests · null distribution · exchangeability · statistical power

## 1 A *p*-value needs a null distribution

In an [earlier note](https://selcukorkmaz.github.io/blog/p-effect-size-ci/#pvalue) I defined a *p*-value as the probability of getting a test statistic at least as extreme as the one observed, computed on the assumption that the null hypothesis and every other assumption of the statistical model are true \[1\]. That sentence hides a step. A probability needs a distribution: the *null distribution*, which says how the test statistic would vary from study to study if the null hypothesis were true. The *p*-value is the area in its tail beyond the observed value.

Take a small pilot trial. Twenty adults with raised blood pressure are randomised, 10 to a lifestyle programme and 10 to usual care, and the outcome is the fall in systolic blood pressure over 12 weeks (Table 1). The programme arm fell by 9.4 mmHg on average and the usual-care arm by 1.9 mmHg, a difference of 7.5 mmHg.

**Table 1.** The pilot data: fall in systolic blood pressure over 12 weeks, in mmHg (negative values are rises). The data are made up for this note and used throughout.

| Arm                   | Fall in each participant           | Mean | SD  |
|-----------------------|------------------------------------|------|-----|
| Programme (*n* = 10)  | 21, 17, 15, 14, 13, 7, 6, 2, 2, −3 | 9.4  | 7.7 |
| Usual care (*n* = 10) | 11, 10, 9, 5, 2, 1, 0, −1, −9, −9  | 1.9  | 7.1 |

Student's two-sample *t*-test gives *t* = 2.25 on 18 degrees of freedom and *p* = 0.037, with a 95% confidence interval for the difference of 0.5 to 14.5 mmHg. The 0.037 is the area of the *t* distribution with 18 degrees of freedom beyond ±2.25. That distribution is the null distribution of the *t* statistic when the outcomes in both arms are independent draws from normal distributions with the same mean and the same standard deviation (SD). Those are assumptions about how the data arose, and the formula takes them on trust.

A permutation test reaches a null distribution by a route that needs neither the normal distribution nor a formula.

## 2 Shuffling the labels

Suppose the programme had no effect on anybody. Then each participant's fall in blood pressure would have been the same whichever arm the randomisation had put them in. The 20 numbers in Table 1 would be fixed, and the only thing chance decided was which 10 of them carried the label "programme". The randomisation could have picked any 10 of the 20; there are 184,756 ways to do that, all equally likely. For each one we can work out the difference in means we would have seen. Those 184,756 differences are the null distribution of the difference, and no theory was needed to get them.

This null hypothesis, that the programme changed nobody's outcome, is the one a randomisation test examines directly \[2\], and it is stronger than "the two arms have the same mean". Fisher set out the idea in 1935 \[3\]. The method goes by two names: a *randomisation test* when, as here, the shuffling mirrors a random allocation that really took place, and a *permutation test* when the groups are treated as samples from populations, though the two names are often used interchangeably \[2\]. I use "permutation test" for both, as most software does, and "shuffle" for one rearrangement of the labels.

**Permutation test for two groups.**

1.  Compute the statistic with the real labels, *T*<sub>obs</sub> (here the difference in means, 7.5 mmHg).
2.  Shuffle the labels, keeping the group sizes, and recompute the statistic, *T*\*.
3.  Do step 2 for every possible allocation (an exact test) or for *B* random ones.
4.  The two-sided *p* is the share of allocations with \|*T*\*\| ≥ \|*T*<sub>obs</sub>\|. With *B* random shuffles, *p* = (*b* + 1)/(*B* + 1), where *b* counts the shuffles that qualify.

![The 20 participants of the pilot trial and the null distribution of the difference in means built by shuffling their labels. The real difference of 7.5 mmHg lies in the right tail: 7,570 of the 184,756 possible allocations are at least as extreme, so p = 0.041.](https://selcukorkmaz.github.io/blog/permutation-test/fig1.svg)

**Figure 1. Building the null distribution by shuffling the labels.** Top: the 20 participants of Table 1, placed by their fall in systolic blood pressure, in the arm that the allocation shown gives them. Colour and shape show the arm each participant was really in, and the vertical marks are the two arm means. Bottom: the difference in means (programme minus usual care) for every allocation counted so far, as a share of them, in 1 mmHg bins. Allocations at least 7.5 mmHg from zero in either direction are shaded. On the interactive page the buttons shuffle the labels once, 100 times or 1,000 times, or show all 184,756 allocations; the static copy shows all of them, with the real allocation at the top. Exactly 7,570 of the 184,756 allocations are at least as extreme as the real one, so the exact *p* = 0.041.

Figure 1 lets you do it. Each shuffle is one alternative history of the trial in which the programme did nothing. Most give a difference within a few mmHg of zero, and the histogram they build is the null distribution. The real difference of 7.5 mmHg sits in its right tail: exactly 7,570 of the 184,756 possible allocations give a difference at least 7.5 mmHg from zero, in either direction, so

*p* = 7,570 / 184,756 = 0.041.

That is the most literal reading a *p*-value can have. If the programme did nothing, 4.1% of the ways the randomisation could have split these 20 people would have produced a gap at least as large as the one observed. It is not the probability that the programme did nothing, nor the probability that the result was produced by chance alone \[4\]; it is computed by assuming that the programme did nothing.

Because the two arms are the same size, the shuffle distribution is symmetric about zero: swapping the two arms of any allocation turns its difference into minus that difference. Counting allocations with \|*T*\*\| ≥ \|*T*<sub>obs</sub>\| then gives exactly twice the one-sided count. With arms of different sizes the distribution need not be symmetric, and the absolute-value rule and doubling the one-sided *p* can disagree, so say which you used.

## 3 Every allocation, or a random sample of them?

Listing every allocation gives the *exact* permutation *p*-value. That is feasible here because 184,756 is a small number for a computer. With 30 participants per arm there are about 1.2 × 10<sup>17</sup> allocations, and with the 65 per arm of the earlier note about 9.5 × 10<sup>37</sup>, so in practice we draw *B* allocations at random and estimate *p* from them. This is a Monte Carlo permutation test, and two details matter.

**Count the real allocation.** Use *p* = (*b* + 1)/(*B* + 1), where *b* is the number of random shuffles at least as extreme as the real data. The real allocation is one of those the randomisation could have produced, and with the +1 the test rejects a true null hypothesis no more often than its stated level. The plain share *b*/*B* can be zero, and it is smaller than (*b* + 1)/(*B* + 1) whenever *b* \< *B*, so a test built on it can reject a true null hypothesis more often than stated \[5\]. A permutation *p*-value can never really be zero \[5\], and the smallest value *B* shuffles can give is 1/(*B* + 1): 999 shuffles cannot give less than 0.001.

**Use enough shuffles.** A Monte Carlo *p*-value has its own sampling error, with a standard error of about √\[*p*(1 − *p*)/*B*\] (Table 2). With 999 shuffles, a test whose exact *p* is 0.041 will usually report something between 0.030 and 0.055, and about one run in eleven will report a value above 0.05. With 9,999 shuffles the range shrinks to 0.037 to 0.045. Choose *B* so that this error is small next to the precision you report. A sensible default for a single test is 9,999 shuffles, and far more are needed when *p*-values will be compared with a very small threshold, as after a correction for multiple testing.

**Table 2.** How precise is a Monte Carlo permutation *p*-value? For the example's exact *p* = 0.041: the standard error √\[*p*(1 − *p*)/*B*\] of a *p*-value estimated from *B* random shuffles, the central range that holds at least 95% of estimates (from the binomial distribution of *b*, with the +1 included), and the smallest *p* that *B* shuffles can give, 1/(*B* + 1).

| Random shuffles, *B* | Standard error | About 95% of estimates | Smallest possible *p* |
|----|----|----|----|
| 99 | 0.020 | 0.020 to 0.090 | 0.01 |
| 999 | 0.0063 | 0.030 to 0.055 | 0.001 |
| 9,999 | 0.0020 | 0.037 to 0.045 | 0.0001 |
| 99,999 | 0.00063 | 0.040 to 0.042 | 0.00001 |

## 4 The *t* distribution is a shortcut

The shuffle distribution in Figure 1 looks like a bell curve, and the comparison with the *t*-test is as old as the method. In *The Design of Experiments* Fisher applied the method to Darwin's data on 15 pairs of maize plants: he counted all 32,768 ways of flipping the signs of the within-pair differences, found that 5.3% of them were at least as extreme as the observed total, and noted that this was very nearly the result of Student's *t*-test \[3\]. A year later he described an imagined two-group comparison as a shuffle of cards: write the statures of a sample of 100 Englishmen and 100 Frenchmen on cards, shuffle them without regard to nationality, and deal them into two new groups of 100. The statistician's conclusions, he wrote, have no justification beyond their agreement with what this elementary method would give \[6\]. Pitman showed in 1937 how to build such tests with no assumption about the form of the populations sampled \[7\]. Figure 2 overlays the shuffle distribution and the *t* distribution. The bars are the exact shuffle distribution of the difference in means. The curve is the null distribution that the *t*-test uses, drawn on the same scale: a *t* distribution with 18 degrees of freedom, stretched by the standard error of the difference (3.33 mmHg), so that its area beyond ±7.5 mmHg is the *t*-test's *p*-value.

![The exact shuffle distribution of the difference in means for the pilot data, with the t distribution used by the t-test drawn on the same scale. The two agree closely: p = 0.041 from the shuffles and 0.037 from the t distribution.](https://selcukorkmaz.github.io/blog/permutation-test/fig2.svg)

**Figure 2. The shuffle distribution and the *t* distribution.** Bars: the exact null distribution of the statistic over all 184,756 allocations, as a share of them in 1 mmHg bins (for medians, one bar for each possible value, 0.5 mmHg apart), with allocations at least as extreme as the observed value shaded. Curve (difference in means only): a *t* variable with 18 degrees of freedom multiplied by the standard error of the difference (3.33 mmHg for the data of Table 1; 4.80 mmHg with the 45 mmHg value), that is, its density stretched by that factor, so that its tail area beyond the dashed lines is the *t*-test's *p*-value. On the interactive page the buttons switch to a data set in which the largest fall in the programme arm is 45 mmHg instead of 21, and to the difference in medians, for which the shuffles work just as well but the *t*-test does not apply. The static copy shows the data of Table 1 and the difference in means. With the 45 mmHg value, the difference in means is 9.9 mmHg, the shuffle *p* = 0.039 and the *t*-test *p* = 0.054; the difference in medians is 8.5 mmHg with shuffle *p* = 0.067 in both data sets.

For the pilot data the two agree well: *p* = 0.041 from the shuffles and 0.037 from the *t* distribution. The confidence intervals agree too, at 0.5 to 14.5 mmHg either way (Section 7). When the data look like these, the *t*-test is a quick and accurate approximation to the exact answer.

They part company when the data do not fit the bell. Switch Figure 2 to the second data set, in which the largest fall in the programme arm is 45 mmHg instead of 21, say because one participant also started a blood pressure drug. The difference in means rises to 9.9 mmHg, but the SD of the programme arm rises from 7.7 to 13.4 mmHg, and the *t*-test gives *p* = 0.054 (Welch's version, 0.059). The shuffle distribution, by contrast, changes shape. The 45 lands in one arm or the other in every allocation and pushes the difference about 4 mmHg in that direction, so the distribution is wider than before but flat-topped, with short tails. Its exact *p*-value is 0.039. The *t* curve, a bell with longer tails, no longer describes what the randomisation could have produced.

That is not an argument that shuffling rescues the mean. With the 45 in the data, the difference in means still depends heavily on one person, and a statistic that resists outliers may answer the question better. Switch the statistic to the difference in medians. The shuffles build its null distribution just as easily, and give *p* = 0.067 for both data sets, because the median ignores how far the largest value lies from the rest. Like any shuffle test, though, it examines whether the two groups are exchangeable: when their distributions differ in shape, its error rate as a test of equal medians can be far from the stated level, even with equal group sizes \[8\]. A permutation test lets you choose the statistic, so choose it before seeing the data: trying several and reporting the one with the smallest *p*-value makes that *p*-value misleading \[1,4\].

## 5 What a shuffle assumes

Shuffling needs no normal distribution, but it is not assumption-free. Its essential assumption is *exchangeability*: if the null hypothesis is true, swapping the labels does not change the probability of the data \[9\]. Where exchangeability comes from depends on how the data arose \[2\].

- **In a randomised trial, the randomisation supplies it.** Every allocation the randomisation could have made was equally likely, and under the null hypothesis that the treatment changed nobody's outcome the outcomes would have been the same under each, so the chance of a false positive is at most the stated level whatever the distribution of the outcome, with no assumption that the participants are a random sample from a population \[2\]. That fits most biomedical experiments: in a survey of 252 comparative studies, Ludbrook and Dudley found groups formed by randomisation in 96% and by random sampling in only 4% \[10\]. The conclusion then concerns the participants in the study \[2\]; extending it to others is a judgement about how they were recruited. The guarantee is for the null hypothesis that nobody's outcome changed. If the programme could change the spread of outcomes without changing their average, a small *p*-value from the raw difference may reflect the spread when the arms differ in size. To test the average effect, shuffle a studentised statistic, described below, which does so approximately in large samples \[11\]; with equal arms, as in the pilot, it gives the same test as the raw difference.
- **In an observational comparison it is an assumption.** Nobody assigned the labels when men are compared with women or smokers with non-smokers. Exchangeability then rests on the null hypothesis that both groups were sampled from the same distribution: the same shape and the same spread, not only the same mean \[2\].

The second point has a practical consequence. Suppose two groups have the same mean but different SDs. The null hypothesis of identical distributions is then false, the labels are not exchangeable, and a shuffle test of the difference in means can reject far more or far less often than its nominal 5%, just as Student's pooled *t*-test does (Table 3). Shuffling a *studentised* statistic, one that divides the difference by its own standard error, as Welch's *t* does, keeps the test exact when the groups are exchangeable and brings its error rate close to the nominal level in large samples when they are not \[12,13\]. With equal group sizes, even the raw difference behaves well in large samples \[8,12\].

**Table 3.** How often each test gives *p* ≤ 0.05 when the two population means are equal (nominal 5%). Normal outcomes; 50,000 simulated data sets per row (simulation standard error about 0.1 percentage points near 5% and 0.2 near 21%); permutation tests with 999 random shuffles each and *p* = (*b* + 1)/(*B* + 1). In the first row Student's *t* and the shuffle tests have a size of exactly 5% in theory; the 5.2% is simulation error.

| Situation | Group sizes | SDs | Student's *t* | Welch's *t* | Shuffle: difference in means | Shuffle: Welch's *t* |
|----|----|----|----|----|----|----|
| Same SD (reference) | 8 and 24 | 1 and 1 | 5.2% | 5.3% | 5.2% | 5.2% |
| Smaller group more variable | 8 and 24 | 3 and 1 | 21.5% | 5.2% | 21.7% | 6.6% |
| Larger group more variable | 8 and 24 | 1 and 3 | 0.4% | 5.0% | 0.4% | 4.0% |
| Equal sizes, different SDs | 16 and 16 | 3 and 1 | 5.6% | 5.0% | 5.7% | 5.7% |

When the smaller group is the more variable one, both Student's *t*-test and the shuffle test of the raw difference reject a true null hypothesis about one time in five; when the larger group is the more variable one, they almost never reject. Shuffling Welch's *t* brings the rates to 6.6% and 4.0%, close to but not at 5%, because with groups of 8 and 24 its protection is only approximate, and Welch's *t*-test with its own *t* distribution does slightly better here. Shuffling does not mend a statistic that ignores unequal spread. With equal group sizes, as in the last row and in the pilot, shuffling Welch's *t* gives exactly the same test as shuffling the raw difference: with equal group sizes Welch's *t* equals Student's *t*, and when only the labels change, Student's *t* rises steadily with the size of the difference.

The design has a consequence too: shuffle only what was randomised, in the way it was randomised (Table 4). The set of allocations the test compares with should be the set the randomisation could actually have produced, each with the probability the randomisation gave it \[9,14\].

**Table 4.** Shuffle what was randomised.

| Design | What to shuffle |
|----|----|
| Two independent groups, complete randomisation (or simple randomisation, conditioning on the group sizes) | the labels of all participants, keeping the group sizes |
| Matched pairs, treatment randomised within each pair | within each pair only: flip the sign of each within-pair difference, which gives 2<sup>*n*</sup> allocations for *n* pairs |
| Crossover trial | the sequence labels (AB or BA) of whole participants, as randomised; for example, compare the period 1 minus period 2 differences between the sequence groups |
| Before and after, nothing randomised | no randomisation to mirror; a sign-flip test can still be run, but it assumes each difference is symmetric about zero under the null hypothesis, which time trends and regression to the mean can break |
| Stratified or blocked randomisation | labels within each stratum or block, never across them |
| Cluster randomisation (practices, wards, schools) | the labels of whole clusters, never of individuals |
| Repeated measures over time | not individual observations, which are not exchangeable; shuffle whole participants, or use a scheme designed for the structure |
| Adjusting for covariates | in a randomised trial, shuffle the treatment labels as they were randomised and recompute the covariate-adjusted statistic; when the variable of interest was not randomised, use a method designed for it, such as permuting residuals (Freedman–Lane), which is approximate \[9\] |

## 6 The *p*-value has a distribution too

A null distribution describes the test statistic across imagined repetitions of a study. The *p*-value is computed from the statistic, so it also varies from one repetition to the next, and its distribution is the clearest way to see what a single *p*-value can tell you \[15,16\]. Figure 3 runs the pilot trial 1,000 times on computer-generated data, with outcomes normally distributed with an SD of 8 mmHg, analyses every run with a permutation test of 999 shuffles, and plots the 1,000 *p*-values.

![Histograms of 1,000 permutation p-values from simulated trials with 10 per arm. With no effect the p-values are spread evenly between 0 and 1; with a true difference of 8 mmHg they pile up near zero, and 53.7% fall at or below 0.05.](https://selcukorkmaz.github.io/blog/permutation-test/fig3.svg)

**Figure 3. The distribution of the *p*-value over 1,000 simulated runs of the trial.** Each run draws participants for both arms from normal distributions with an SD of 8 mmHg, differing in mean by the true difference, and computes a two-sided permutation *p*-value for the difference in means from 999 random shuffles. Bars show the share of runs in each 0.05-wide bin of *p*; the first bin, *p* ≤ 0.05, is shaded. The dashed line at 5% is what each bin holds on average when there is no effect. Left: no effect. Right: the true difference chosen with the buttons (4, 8 or 12 mmHg). On the interactive page the buttons also switch between 10 and 20 participants per arm; the static copy shows 8 mmHg and 10 per arm.

- **No effect.** The *p*-values are spread evenly between 0 and 1, and each 0.05-wide bin holds about 5% of the runs. That is what a valid test does: when the null hypothesis and the model are true and the test statistic is continuous, *p* is equally likely to fall anywhere between 0 and 1, so *p* ≤ 0.05 happens in about 5% of runs (4.3% in this simulation), which is all a 5% significance level promises \[15,17\]. For a Monte Carlo permutation test with continuous data, the real data's rank among the *B* + 1 values is then equally likely to be any of 1, …, *B* + 1, apart from the small chance that a random shuffle reproduces the real allocation or its mirror image (the two arms swapped), so (*b* + 1)/(*B* + 1) takes each of the values 1/(*B* + 1), 2/(*B* + 1), …, 1 with almost exactly equal probability.
- **A real effect.** The *p*-values pile up near zero \[15\], and the share at or below 0.05 is, by definition, the power of the test for that effect \[17\]. With a true difference of 8 mmHg, one SD, and 10 participants per arm, the power is only about 56% (the 1,000 runs in Figure 3 give 53.7%, within simulation error): the same trial, repeated with the same true effect, would give *p* above 0.05 nearly half the time. In the long run the median *p* is about 0.04, close to the pilot's, but the middle 80% of *p*-values run from about 0.002 to about 0.35 (the 1,000 runs in Figure 3 give 0.002 to 0.38).

The pilot's *p* = 0.041 is one draw from a distribution like the right-hand one. A repeat of the trial could easily give 0.3 or 0.002 \[16\]. So a single *p*-value says little about whether a result will replicate, and the estimate and its confidence interval, which show the size of the effect and the precision of the study, carry more of what a reader needs.

## 7 Intervals from shuffles, and the bootstrap

A permutation test answers a question about one hypothesis, but like any test it can be turned into a confidence interval. Assume a shift model, in which the programme lowers everyone's blood pressure by the same amount *δ*. For a candidate *δ*, subtract it from each programme value and run the shuffle test of "no effect" on the shifted data. The 95% interval is the set of *δ* values whose *p*-value is above 0.05 \[2\]: the stretch where the [*p*-value function](https://selcukorkmaz.github.io/blog/p-effect-size-ci/#ci) of the earlier note, built here from shuffles instead of from the *t* distribution, lies above 0.05. For the pilot data it runs from 0.5 to 14.5 mmHg, the same as the *t* interval to one decimal place. For the data with the 45 mmHg value it runs from 0.6 to 20.0 mmHg, where the *t* interval is −0.2 to 20.0.

The bootstrap is the other resampling method in common use, and the two are easy to confuse. They answer different questions (Table 5).

**Table 5.** Shuffle or resample? Permutation tests and the bootstrap compared \[2,18\].

|  | Permutation test | Bootstrap |
|----|----|----|
| **Question** | Are the data compatible with a stated null hypothesis? | How much would the estimate vary from sample to sample? |
| **What is resampled** | the labels, rearranged without replacement, keeping the group sizes | the participants, drawn with replacement, usually within each group |
| **Null hypothesis built in?** | yes, by construction | no; a bootstrap test either inverts a confidence interval or resamples in a way consistent with the null hypothesis |
| **Main output** | *p*-value; an interval by inversion under a shift model | standard error and confidence interval |
| **Key assumption** | exchangeability under the null hypothesis | the sample stands in for the population; percentile intervals tend to be too narrow in small samples |

## 8 How to report a permutation test

**Rule of thumb.** Name the statistic, say what was shuffled and within what, say whether the *p*-value comes from all allocations (an exact *p*-value) or from random shuffles (and how many), and report the estimate with its confidence interval as for any other test.

A permutation *p*-value is still a *p*-value, and the [reporting advice of the earlier note](https://selcukorkmaz.github.io/blog/p-effect-size-ci/#report) applies to it, starting with the estimate and its interval. The methods section needs enough extra detail for someone else to get the same number:

- **The statistic**, chosen in advance: difference in means, difference in medians, Welch's *t*, or another.
- **What was shuffled**, and within what: strata, blocks, pairs or clusters, matching the randomisation.
- **All allocations or random shuffles.** For random shuffles (a Monte Carlo test), the number of shuffles *B*, the formula (*b* + 1)/(*B* + 1), the software and the random seed.
- **The sidedness**, and for groups of different sizes, how the two-sided *p* was defined.
- **The estimate and its interval**, with the method for the interval: a *t* interval, a bootstrap interval, or one from inverting the permutation test.

### 8.1 Sentences to adapt

- **Methods, exact test.** "The difference in mean fall in systolic blood pressure (programme minus usual care) was tested with a two-sided exact permutation test, using all 184,756 ways of allocating the 20 participants to two groups of 10; the *p*-value was the proportion of allocations whose difference was at least as far from zero as the observed one."
- **Methods, Monte Carlo test.** "The difference in means was tested with a two-sided permutation test, using 9,999 random reallocations of the treatment labels (R 4.5.2, seed 2026), made within randomisation strata if the trial was stratified. The *p*-value was computed as (*b* + 1)/(*B* + 1), where *b* is the number of reallocations giving a difference at least as far from zero as the observed one and *B* = 9,999."
- **Results.** "Systolic blood pressure fell 7.5 mmHg more in the programme group than in the usual-care group (95% CI 0.5 to 14.5, from inverting the permutation test; exact permutation *p* = 0.041)."

Base R does both versions in a few lines. The small tolerance in the comparisons keeps allocations whose difference equals the observed one, which rounding error could otherwise drop.

``` r
prog  <- c(21, 17, 15, 14, 13, 7, 6, 2, 2, -3)
usual <- c(11, 10, 9, 5, 2, 1, 0, -1, -9, -9)
x <- c(prog, usual); n1 <- length(prog); n2 <- length(usual)
obs <- mean(prog) - mean(usual)                       # 7.5

# Exact: every choice of the 10 participants labelled "programme"
idx  <- combn(n1 + n2, n1)                            # 184,756 allocations
sA   <- colSums(matrix(x[idx], nrow = n1))
diff <- sA / n1 - (sum(x) - sA) / n2
mean(abs(diff) >= abs(obs) - 1e-8)                    # 0.04097 (7,570 of 184,756)

# Monte Carlo: B random shuffles, counting the real allocation
set.seed(2026)
B   <- 9999
sim <- replicate(B, { s <- sample(x); mean(s[1:n1]) - mean(s[-(1:n1)]) })
(sum(abs(sim) >= abs(obs) - 1e-8) + 1) / (B + 1)      # 0.0421

t.test(prog, usual, var.equal = TRUE)                 # t = 2.253, df = 18, p = 0.03697
```

## 9 Five traps

### 9.1 Reporting *p* = 0

If none of 999 shuffles is as extreme as the real data, the *p*-value is (0 + 1)/(999 + 1) = 0.001, the smallest that 999 shuffles can give, not zero \[5\]. Report it as *p* = 0.001 with the number of shuffles, or use more shuffles.

### 9.2 Too few shuffles for the question

The Monte Carlo error in Table 2 matters most near a threshold and after a multiplicity correction. With 1,000 tests and a Bonferroni threshold of 0.05/1,000 = 0.00005, a test with 999 shuffles can never reach it, because its smallest possible *p* is 0.001. Reaching the threshold at all takes at least 19,999 shuffles, and estimating *p* well near it takes many more.

### 9.3 Shuffling what was not randomised

Shuffling individuals in a cluster-randomised trial, or across strata in a stratified one, compares the data with allocations the randomisation could never have produced. Treating the participants of a cluster trial as independent pretends there are more independent units than there are, which usually makes the *p*-value too small. Follow Table 4.

### 9.4 Reading "non-parametric" as "assumption-free"

A shuffle test of the difference in means compares the data with the null hypothesis that the two groups are exchangeable. In an observational comparison, or for a treatment that may change the spread of outcomes, that means identical distributions, so a small *p*-value can reflect a difference in spread or shape rather than in the means, and groups of unequal size and spread can make the error rate far from nominal (Table 3).

### 9.5 Choosing the statistic after seeing the data

For the pilot data, the shuffle test gives *p* = 0.041 for the difference in means and 0.067 for the difference in medians. Both are legitimate, but only one was the plan. Name the statistic in the protocol or the analysis plan, and if you report others, say so and report them all \[1,4\].

## 10 A checklist for authors and reviewers

- The statistic was chosen in advance and is named.
- What was shuffled matches the design: individuals, pairs, clusters, and within which strata or blocks.
- The methods say whether *p* comes from all allocations or from random shuffles; for random shuffles they give the number of shuffles, the formula (*b* + 1)/(*B* + 1), the software and the seed.
- The number of shuffles is large enough for the precision reported and for any multiplicity threshold.
- No *p*-value is reported as 0.
- For a difference in means between groups of unequal size and spread, a studentised statistic was shuffled or Welch's test was used.
- Two-sided *p*-values say how the two tails were counted when the groups differ in size.
- The estimate and its confidence interval are reported alongside, with the method for the interval.

A permutation test turns the null distribution into something you can watch being built. Every *p*-value has one, whether it comes from a formula or from shuffles, and a *p*-value means only as much as the null distribution behind it.

## References

1.  Greenland S, Senn SJ, Rothman KJ, et al. Statistical tests, P values, confidence intervals, and power: a guide to misinterpretations. *European Journal of Epidemiology*. 2016;31(4):337–350. doi:10.1007/s10654-016-0149-3
2.  Ernst MD. Permutation methods: a basis for exact inference. *Statistical Science*. 2004;19(4):676–685. doi:10.1214/088342304000000396
3.  Fisher RA. *The Design of Experiments*. Oliver and Boyd; 1935.
4.  Wasserstein RL, Lazar NA. The ASA statement on *p*-values: context, process, and purpose. *The American Statistician*. 2016;70(2):129–133. doi:10.1080/00031305.2016.1154108
5.  Phipson B, Smyth GK. Permutation P-values should never be zero: calculating exact P-values when permutations are randomly drawn. *Statistical Applications in Genetics and Molecular Biology*. 2010;9(1):Article 39. doi:10.2202/1544-6115.1585
6.  Fisher RA. "The coefficient of racial likeness" and the future of craniometry. *Journal of the Royal Anthropological Institute of Great Britain and Ireland*. 1936;66:57–63. doi:10.2307/2844116
7.  Pitman EJG. Significance tests which may be applied to samples from any populations. *Supplement to the Journal of the Royal Statistical Society*. 1937;4(1):119–130. doi:10.2307/2984124
8.  Romano JP. On the behavior of randomization tests without a group invariance assumption. *Journal of the American Statistical Association*. 1990;85(411):686–692. doi:10.1080/01621459.1990.10474928
9.  Winkler AM, Ridgway GR, Webster MA, Smith SM, Nichols TE. Permutation inference for the general linear model. *NeuroImage*. 2014;92:381–397. doi:10.1016/j.neuroimage.2014.01.060
10. Ludbrook J, Dudley H. Why permutation tests are superior to *t* and *F* tests in biomedical research. *The American Statistician*. 1998;52(2):127–132. doi:10.1080/00031305.1998.10480551
11. Wu J, Ding P. Randomization tests for weak null hypotheses in randomized experiments. *Journal of the American Statistical Association*. 2021;116(536):1898–1913. doi:10.1080/01621459.2020.1750415
12. Chung E, Romano JP. Exact and asymptotically robust permutation tests. *The Annals of Statistics*. 2013;41(2):484–507. doi:10.1214/13-AOS1090
13. Janssen A. Studentized permutation tests for non-i.i.d. hypotheses and the generalized Behrens–Fisher problem. *Statistics & Probability Letters*. 1997;36(1):9–21. doi:10.1016/S0167-7152(97)00043-6
14. Rosenberger WF, Uschner D, Wang Y. Randomization: the forgotten component of the randomized clinical trial. *Statistics in Medicine*. 2019;38(1):1–12. doi:10.1002/sim.7901
15. Murdoch DJ, Tsai YL, Adcock J. *P*-values are random variables. *The American Statistician*. 2008;62(3):242–245. doi:10.1198/000313008X332421
16. Halsey LG, Curran-Everett D, Vowler SL, Drummond GB. The fickle *P* value generates irreproducible results. *Nature Methods*. 2015;12(3):179–185. doi:10.1038/nmeth.3288
17. Sackrowitz H, Samuel-Cahn E. *P* values as random variables—expected *P* values. *The American Statistician*. 1999;53(4):326–331. doi:10.1080/00031305.1999.10474484
18. Hesterberg TC. What teachers should know about the bootstrap: resampling in the undergraduate statistics curriculum. *The American Statistician*. 2015;69(4):371–386. doi:10.1080/00031305.2015.1089789
