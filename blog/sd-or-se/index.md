# Standard deviation or standard error?

*What each one measures, and which one belongs in your paper*

Statistics note · Reporting in biomedical research

> Source: https://selcukorkmaz.github.io/blog/sd-or-se/ · 28 September 2026

Selçuk Korkmaz\
28 September 2026

## In short

The standard deviation (SD) and the standard error (SE) look alike, share most of a formula, and are swapped for each other in published papers all the time. They answer different questions. The SD describes the *data*: how far individual observations typically fall from their mean. The SE describes an *estimate*: how far that mean, or a difference, a proportion or a regression coefficient, would typically move if the study were repeated with new participants. As a sample grows, the SD settles near the population value, while the SE keeps shrinking in proportion to 1/√*n*.

The rule for papers follows from that. Use the SD, or the median and interquartile range for skewed data, when you describe your sample. Use a 95% confidence interval when you report what you estimated. The SE is mainly a building block for intervals and tests. On its own, and above all as an error bar, it tends to mislead. Two interactive figures below show why, and Table 3 maps common situations in a manuscript to what to report.

Keywords: standard deviation · standard error · confidence intervals · error bars · statistical reporting · SAMPL

## 1 A familiar line in a results table

Suppose a table describing 120 patients reports `Age, years: 54.2 ± 1.1`. What does the 1.1 mean? If it is an SD, the cohort is remarkably uniform: assuming roughly normal ages, about two thirds of the patients are between 53.1 and 55.3 years old. If it is an SE, the SD is 1.1 × √120 ≈ 12.0 years, and the patients span several decades. These are two very different cohorts, and the line alone does not say which one the study enrolled.

The ambiguity is common. In a review of 860 articles published in four anaesthesia journals in 2001, 198 (23%) used the standard error of the mean where the variability of the sample should have been described \[1\]. The confusion extends to figures. When 473 authors of articles in psychology, behavioural neuroscience and medicine were shown two means with error bars and asked to move one of them until the difference was just statistically significant, many showed serious misconceptions about how SE bars and confidence-interval bars relate to significance \[2\].

The misuse persists for a simple reason. For any sample with more than one observation, the SE is smaller than the SD, so it makes data look tidier and differences look more convincing. That is the reason it misleads readers about the variability of the sample when it is used to describe data \[1\].

## 2 Two quantities, two questions

Both quantities start from the same sample of *n* observations *x*<sub>1</sub>, …, *x*<sub>*n*</sub> with mean *x̄*.

SD = *s* = √\[Σ (*x*<sub>*i*</sub> − *x̄*)<sup>2</sup> / (*n* − 1)\]

SE(*x̄*) = *s* / √*n*

**The standard deviation** answers the question *how different are the individuals?* It is the typical distance of an observation from the mean, and it estimates σ, the SD of the population being sampled. It is a property of that population, together with any measurement error. For roughly normal data, about 68% of observations lie within one SD of the mean and about 95% within 1.96 SD. That is why mean ± 2 SD serves as a rough reference range for individuals.

**The standard error** answers the question *how precisely do we know the mean?* Imagine running the same study many times, each time drawing *n* new participants and computing their mean. The means would scatter around the population mean μ, and the SD of that scatter would be σ/√*n*. The SE estimates this quantity from the one sample actually collected. It is a property of the estimate and of the design, not of the participants \[3\].

**The key sentence.** The standard error *is* a standard deviation: the standard deviation of an estimate across hypothetical repeats of the study, not of the data within one study. Most of the confusion comes from the shared name, and most of it goes away once that sentence is clear.

Every estimate has its own SE, not only the mean (Table 1). A 95% confidence interval (CI) is built from the SE and a multiplier from the *t* or normal distribution. The CI is what readers can actually interpret: under the model's assumptions, it gives the range of population values compatible with the data at the 95% level.

**Table 1.** Standard errors of common estimates and the 95% confidence interval built from them. *s*, sample SD; *p*, sample proportion; *t*<sub>0.975, *n*−1</sub>, the 97.5th percentile of the *t* distribution with *n* − 1 degrees of freedom.

| Estimate | Standard error | Notes |
|----|----|----|
| Mean *x̄* | *s* / √*n* | 95% CI: *x̄* ± *t*<sub>0.975, *n*−1</sub> × SE |
| Proportion *p* | √\[*p*(1 − *p*) / *n*\] | Wald form; prefer Wilson or exact intervals for small *n* or *p* near 0 or 1 |
| Difference of two independent means | √\[*s*<sub>1</sub><sup>2</sup>/*n*<sub>1</sub> + *s*<sub>2</sub><sup>2</sup>/*n*<sub>2</sub>\] | Welch form; the CI uses Welch–Satterthwaite degrees of freedom |
| Mean of paired differences | *s*<sub>*d*</sub> / √*n* | *s*<sub>*d*</sub> is the SD of the within-pair differences, not of either measurement |
| Regression coefficient | From the model's variance–covariance matrix | Printed by the software next to each coefficient |

Figure 1 puts the two quantities on the same axis. The population is fixed: systolic blood pressure with mean 128 mmHg and SD 16 mmHg. Change the sample size and watch which bars move.

![A sample from a normal population with its mean plus or minus one SD, one SE and its 95% confidence interval, and below it the means of 2,000 samples of the same size.](https://selcukorkmaz.github.io/blog/sd-or-se/fig1.svg)

**Figure 1. The SD describes the people; the SE describes the mean.** The population (grey curve) is normal with mean 128 mmHg and SD 16 mmHg. (a) One random sample of size *n*, with three intervals around its mean: ± 1 SD, ± 1 SE and the 95% CI. (b) The means of 2,000 further samples of the same size from the same population, on the same axis. The spread of these means across repeated studies is what the SE in (a) estimates from a single sample. As *n* increases, the SD bar stays close to the width of the population curve, while the SE bar, the CI and the histogram in (b) narrow together.

## 3 Why one shrinks and the other does not

A larger sample gives a more precise estimate of σ, but the sample SD does not get smaller on average; it settles near σ. In very small samples it runs slightly low: its expected value is about 94% of σ at *n* = 5 and about 99% at *n* = 25. The SE, in contrast, is divided by √*n*, so quadrupling the sample halves it (Figure 2).

![As sample size increases from 3 to 1,000 on a log scale, the SD stays near 16 mmHg while the SE and the 95% CI half-width fall towards zero.](https://selcukorkmaz.github.io/blog/sd-or-se/fig2.svg)

**Figure 2. The SD settles; the SE keeps shrinking.** Lines show the population values for the blood-pressure example: σ = 16 mmHg (SD), σ/√*n* (SE), and the half-width of the 95% CI for the mean, *t*<sub>0.975, *n*−1</sub> × σ/√*n* (dashed). Points show one simulated sample at each size. The horizontal axis is logarithmic. For *n* ≤ 6 the 95% CI for the mean extends further on each side than one SD, because the *t* multiplier is large when the SD itself is poorly estimated.

This has a practical consequence. The SE mixes two things, the variability of the participants and the size of the study. Two studies of the same kind of patients, one with 20 and one with 500 participants, report very different SEs for the same variable. A reader who wants to know how variable the patients were has to recover *n* and multiply by √*n*, and many will not. The SD gives that information directly. The reverse also holds: an SD alone does not say how precisely the mean is known unless *n* is given as well. Each quantity has its job, and neither can do the other's.

## 4 Error bars: what a reader can and cannot infer

A figure of group means with error bars can show SD, SE or CI bars, and the three look alike. The first two rules for any such figure are to state in the legend which one is shown and what *n* is, where *n* counts independent experiments or participants rather than replicates \[4\]. After that, each type supports different conclusions.

- **SD bars** show the spread of the data. Their width does not depend on *n*. Whether the SD bars of two groups overlap depends on the size of the difference relative to the spread: if the ± 1 SD bars do not overlap, the means differ by more than the sum of the two SDs (about two SDs when they are similar), which is a very large effect. Overlap of SD bars says nothing direct about statistical significance.
- **SE bars** are short, and that is their danger. In large samples ± 1 SE is roughly a 68% confidence interval; with *n* = 3 it covers only about 58%. For two independent groups of similar size and spread, with at least about 10 per group, SE bars that just touch correspond to *p* ≈ 0.16 \[2\], and a gap of about one SE between the bars is needed before *p* ≈ 0.05 \[4,5\]. With 3 per group, the same calculation gives *p* ≈ 0.23 for touching SE bars, and the gap must be about two SEs before *p* ≈ 0.05 \[4\]. Bars that do not overlap are therefore not evidence of a difference.
- **95% CI bars** have a fixed meaning for inference. For two independent groups with at least about 10 per group and CIs of similar width, 95% CIs that just touch correspond to *p* ≈ 0.006, and an overlap of about half an arm corresponds to *p* of about 0.03 to 0.04, which the usual rule of thumb rounds conservatively to *p* ≈ 0.05 \[4,5\]. Overlapping CIs therefore do not imply that the difference is not significant. With fewer per group the *t* multiplier widens the CIs, so the same overlap goes with even smaller *p*-values: with 3 per group, half an arm of overlap corresponds to *p* ≈ 0.01 \[4\].

The size of the gap between SE bars and CI bars depends on *n* through the *t* multiplier (Table 2). In laboratory studies with three independent experiments per group, SE bars show less than a quarter of the width of the 95% CI.

**Table 2.** Half-width of the 95% CI for a mean, in units of the SE (*t*<sub>0.975, *n*−1</sub>).

| *n*                    | 3    | 5    | 10   | 20   | 30   | 100  | ∞    |
|------------------------|------|------|------|------|------|------|------|
| 95% CI = mean ± … × SE | 4.30 | 2.78 | 2.26 | 2.09 | 2.05 | 1.98 | 1.96 |

These rules of thumb have two limits. First, they apply only to independent groups. When the same participants are measured twice, the bars on each mean say nothing about the within-participant change, which can be precisely estimated even when the two sets of bars overlap heavily. Show the mean of the paired differences with its own CI instead \[4,5\]. In the study of 473 authors, only 11% of those shown a repeated-measures version of the task recognised this problem \[2\]. Second, with small samples, show the data. Very different distributions can produce the same bar chart, and with *n* of 3 to 10 per group there is no reason to hide the individual points \[6\].

Figure 3 draws one dataset with each kind of bar. Changing the bar type changes only the picture; the data and the test result stay the same. With the data first shown (10 per group), the SE bars are clearly separated, yet *p* = 0.09. Switching to 30 per group draws a new, larger dataset; with 95% CI bars its intervals overlap, yet *p* = 0.02.

![Two groups of individual observations with their means and error bars, and on the right the difference between the groups with its 95% confidence interval.](https://selcukorkmaz.github.io/blog/sd-or-se/fig3.svg)

**Figure 3. The same two groups, three kinds of error bar.** Simulated data from two independent normal populations with means 100 and 112 and a common SD of 15, so the true difference is 0.8 SD. Dots are individual observations, and the short horizontal line on each bar marks the group mean. The panel on the right shows the difference in means (treated − control) with its Welch 95% CI, on the same scale, with zero aligned to the control mean. That interval answers the question the reader actually has, whichever bars are chosen on the left. Changing the group size or pressing "New data" draws a new pair of samples.

## 5 What goes where in a paper

**Rule of thumb.** Describe with the SD; infer with the confidence interval. The SE belongs in the methods, as the ingredient of the interval, or in a regression table next to the CI. It rarely needs to appear on its own.

Reporting guidelines agree on this. The SAMPL guidelines ask authors to summarise approximately normal data as mean (SD), written in that form rather than mean ± SD, not to use the SE to describe the variability of a sample, and to report the precision of estimates with confidence intervals \[7\]. The statistical guidelines of the American Physiological Society make the same distinction: report variability with the SD and uncertainty with a CI \[8\]. The CONSORT 2025 explanation and elaboration document asks trial reports to describe baseline variability with SDs, because SEs and CIs are inferential rather than descriptive, and to give each outcome's effect estimate with its precision, such as a 95% CI \[9\]. The ICMJE recommendations likewise ask authors to present findings with appropriate measures of uncertainty, such as confidence intervals, rather than relying on hypothesis tests alone \[10\].

**Table 3.** What to report in common situations.

| Situation | Report | Avoid |
|----|----|----|
| Describing the sample: a roughly symmetric continuous variable (e.g. baseline table) | mean (SD) | mean ± SE; an unlabelled ± |
| Describing the sample: a skewed variable (length of stay, CRP, costs) | median (IQR), or median (range) for small samples | mean (SD) when the mean is smaller than twice the SD |
| Describing the sample: a categorical variable | *n* (%) | percentages without denominators |
| Baseline table of a randomised trial | descriptive statistics by arm | SEs, CIs and *p*-values for baseline differences |
| Estimating a mean, proportion or rate | estimate with 95% CI | estimate ± SE with no label |
| Comparing groups (the main result) | difference or ratio with 95% CI; *p*-value if needed | a *p*-value alone; each group's SE instead of the CI of the difference |
| Paired or repeated measurements | mean change with 95% CI of the paired difference | separate error bars for each time point as the basis for inference |
| Regression models | coefficient (or OR, HR) with 95% CI; SE optional as an extra column | SE alone, or stars in place of intervals |
| Figures with small *n* | all data points, with the mean or median; bars labelled | bar charts with SE whiskers ("dynamite plots") |
| Figures used for inference about means | 95% CI bars, legend states type and *n* | unlabelled error bars |
| Laboratory experiments with replicates | *n* = independent units (animals, patients, cultures); SD or CI across those units | SE computed over technical replicates |
| Anything a meta-analyst might need | *n*, mean and SD for each group | SE or CI only, without *n* |

In practice the difference is a matter of a few words. Sentences like these make the quantity unambiguous:

- **Methods.** "Continuous variables are summarised as mean (SD) when approximately symmetric and as median (interquartile range) otherwise. Differences between groups are reported with 95% confidence intervals."
- **Baseline.** "The mean age was 54.2 years (SD 12.0); the median length of stay was 5 days (IQR 3 to 9)."
- **Main result.** "At 12 weeks, mean systolic blood pressure was 6.2 mmHg lower in the intervention group than in the control group (95% CI 0.6 to 11.8; *p* = 0.03)."
- **Figure legend.** "Points are individual animals (*n* = 6 per group; each point is the mean of three technical replicates). Horizontal lines show group means; error bars show 95% confidence intervals."

All three quantities take one line each in R:

``` r
n <- length(x)
sd(x)                  # standard deviation: spread of the data
sd(x) / sqrt(n)        # standard error of the mean
t.test(x)$conf.int     # 95% CI: mean(x) ± qt(0.975, n - 1) * SE
t.test(y ~ group, data = d)$conf.int   # Welch 95% CI for a difference in means
```

## 6 Four traps

### 6.1 The bare ± sign

"54.2 ± 1.1" invites the reader to picture a range from 53.1 to 55.3 that holds most of the data. For an SD, that range holds only about two thirds of normally distributed data; for an SE, it says nothing about individuals at all. The notation does not even say whether the second number is an SD or an SE \[3\], and SAMPL recommends the form mean (SD) instead \[7\]. If a journal's style requires ±, state what follows the sign in the methods and in every table footnote and figure legend.

### 6.2 Skewed variables

The SD is a good summary only for roughly symmetric distributions. A quick check works from the summary statistics alone. For a variable that must be positive, such as a length of stay, a concentration or a cost, a mean smaller than twice the SD means the data are likely to be skewed, because a normal distribution extends more than two SDs either side of its mean and would then reach below zero \[11\]. A length of stay of 8.1 days (SD 9.4) is an example; the median and interquartile range describe such data far better. This is a problem of description, not inference. In large samples a CI for the mean based on the SE remains approximately valid even for skewed data, unless the skew is extreme, so the mean with its CI can still be the right estimate when the mean itself (total bed-days, total cost) is the quantity of interest.

### 6.3 The wrong *n*

SE = SD/√*n* assumes *n* independent units. Technical replicates are not independent: repeated wells from the same culture, repeated readings on the same sample or many cells from the same animal. With three mice and ten wells per mouse, *n* is 3, not 30. An SE computed over the 30 wells treats them as independent. If the wells from one mouse agree closely, it understates the true SE about three- to four-fold (roughly √10, the square root of the number of wells per mouse), and a 95% CI built from it uses 29 degrees of freedom instead of 2, so it can come out up to about eight times too narrow \[12\]. Summarise each independent unit first (for example, average the wells for each mouse) and compute the SD and CI across units, or fit a model with a random effect for the unit.

### 6.4 Meta-analyses need SDs

A meta-analysis of a continuous outcome needs *n*, the mean and the SD for each group. When only the SE of a group mean is reported, the SD can be recovered as SE × √*n*, where *n* is the size of that group. From a 95% CI for a group mean it is √*n* × (upper − lower) / 3.92 when the group is large (more than about 100); when it is small (fewer than about 60), 3.92 is replaced by 2 × *t*<sub>0.975, *n*−1</sub>, and in between the *t* version is the safer choice \[13\]. The danger is an unlabelled SE that a meta-analyst reads as an SD. The study's variance is then understated by a factor of *n* and its inverse-variance weight inflated by the same factor: a trial with 100 participants per arm would count as much as 100 such trials. Clear labels protect your study from this misuse.

## 7 A checklist for authors and reviewers

- Every ± sign and every error bar says what it is (SD, SE or 95% CI) and gives *n*.
- Descriptive tables use mean (SD) or median (IQR) and never the SE.
- For positive variables whose mean is smaller than twice the SD, the median (IQR) is reported instead of, or alongside, the mean (SD).
- Main effects are reported as an estimate with a 95% CI, not as a *p*-value alone and not as separate SEs for each group.
- Figures use 95% CIs for inference and SDs for spread, and show the individual points when *n* is small.
- Paired and repeated-measures designs report the CI of the within-participant difference.
- *n* counts independent units; technical replicates are averaged or modelled.
- The paper gives *n*, mean and SD for each group, so that it can be included in a meta-analysis.

Keep the two questions apart and the two quantities follow: the SD tells readers what the participants were like, and the CI, built from the SE, tells them how much the study learned \[3,14\].

## References

1.  Nagele P. Misuse of standard error of the mean (SEM) when reporting variability of a sample. A critical evaluation of four anaesthesia journals. *British Journal of Anaesthesia*. 2003;90(4):514–516. doi:10.1093/bja/aeg087
2.  Belia S, Fidler F, Williams J, Cumming G. Researchers misunderstand confidence intervals and standard error bars. *Psychological Methods*. 2005;10(4):389–396. doi:10.1037/1082-989X.10.4.389
3.  Altman DG, Bland JM. Standard deviations and standard errors. *BMJ*. 2005;331(7521):903. doi:10.1136/bmj.331.7521.903
4.  Cumming G, Fidler F, Vaux DL. Error bars in experimental biology. *Journal of Cell Biology*. 2007;177(1):7–11. doi:10.1083/jcb.200611141
5.  Cumming G, Finch S. Inference by eye: confidence intervals and how to read pictures of data. *American Psychologist*. 2005;60(2):170–180. doi:10.1037/0003-066X.60.2.170
6.  Weissgerber TL, Milic NM, Winham SJ, Garovic VD. Beyond bar and line graphs: time for a new data presentation paradigm. *PLoS Biology*. 2015;13(4):e1002128. doi:10.1371/journal.pbio.1002128
7.  Lang TA, Altman DG. Basic statistical reporting for articles published in biomedical journals: the “Statistical Analyses and Methods in the Published Literature” or the SAMPL Guidelines. *International Journal of Nursing Studies*. 2015;52(1):5–9. doi:10.1016/j.ijnurstu.2014.09.006
8.  Curran-Everett D, Benos DJ. Guidelines for reporting statistics in journals published by the American Physiological Society. *Advances in Physiology Education*. 2004;28(3):85–87. doi:10.1152/advan.00019.2004
9.  Hopewell S, Chan AW, Collins GS, et al. CONSORT 2025 explanation and elaboration: updated guideline for reporting randomised trials. *BMJ*. 2025;389:e081124. doi:10.1136/bmj-2024-081124
10. International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals. https://www.icmje.org/recommendations/
11. Altman DG, Bland JM. Detecting skewness from summary information. *BMJ*. 1996;313(7066):1200. doi:10.1136/bmj.313.7066.1200
12. Vaux DL, Fidler F, Cumming G. Replicates and repeats—what is the difference and is it significant? A brief discussion of statistics and experimental design. *EMBO Reports*. 2012;13(4):291–296. doi:10.1038/embor.2012.36
13. Higgins JPT, Li T, Deeks JJ (editors). Chapter 6: Choosing effect measures and computing estimates of effect (section 6.5.2.2; last updated August 2023). In: Higgins JPT, Thomas J, Chandler J, et al. (editors). *Cochrane Handbook for Systematic Reviews of Interventions*, version 6.5. Cochrane; 2024. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-06
14. Curran-Everett D. Explorations in statistics: standard deviations and standard errors. *Advances in Physiology Education*. 2008;32(3):203–208. doi:10.1152/advan.90123.2008
