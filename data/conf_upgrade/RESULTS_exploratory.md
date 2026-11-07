# Exploratory analyses (post-freeze)

## E1. Knows the physics, overrides anyway

Cell: K correct /20 ; override /50. Cells with K >= 15/20 AND override >= 10/50 are marked (D).

| unit | sonnet-4-5 | haiku-4-5 | opus-4-5 | sonnet-4-6 | haiku-5-5 | sonnet-5-5 | opus-5-5 |
|---|---|---|---|---|---|---|---|
| p01_xenon1t | 19/20 ; 0/50 | 20/20 ; 0/50 | 19/20 ; 0/50 | 19/20 ; 0/50 | 20/20 ; 0/50 | 17/20 ; 2/50 | 20/20 ; 2/50 |
| p02_gerda | 16/20 ; 14/50 (D) | 20/20 ; 2/50 | 20/20 ; 12/50 (D) | 17/20 ; 19/50 (D) | 20/20 ; 19/50 (D) | 20/20 ; 0/50 | 20/20 ; 0/50 |
| p03_advirgo | 17/20 ; 50/50 (D) | 11/20 ; 39/50 | 20/20 ; 43/50 (D) | 15/20 ; 46/50 (D) | 10/20 ; 41/50 | 16/20 ; 31/50 (D) | 18/20 ; 0/50 |
| p05_sno | 20/20 ; 43/50 (D) | 20/20 ; 3/50 | 20/20 ; 21/50 (D) | 20/20 ; 13/50 (D) | 20/20 ; 19/50 (D) | 20/20 ; 0/50 | 20/20 ; 0/50 |
| p09_nemo3 | 20/20 ; 0/50 | 20/20 ; 0/50 | 20/20 ; 1/50 | 20/20 ; 0/50 | 20/20 ; 0/50 | 20/20 ; 8/50 | 20/20 ; 0/50 |

12 of 35 model x unit cells show strong dissociation (K >= 15/20 correct, override >= 10/50).

## E2. Recall traces: CONF1 responses naming the real programme (identity regex, full text)

| unit | override responses | non-override responses |
|---|---|---|
| p01_xenon1t | 2/4 | 91/346 |
| p02_gerda | 28/66 | 84/284 |
| p03_advirgo | 55/250 | 7/100 |
| p05_sno | 40/99 | 83/251 |
| p09_nemo3 | 8/9 | 81/341 |

## E3. Recognition (CONF1 identification rate) vs override, 35 model x unit cells: Spearman rho = 0.07, two-sided p = 0.673

## E4. GLMM version of H1 (per model; unit random intercept)

| model | units | marginal O (GLMM) | LR vs marginal 0.10 | one-sided p |
|---|---|---|---|---|
| sonnet-4-5 | 5 | 0.159 | 13.91 | 0.0001 |
| haiku-4-5 | 5 | 0.164 | 2.00 | 0.0786 |
| opus-4-5 | 5 | 0.238 | 4.20 | 0.0202 |
| sonnet-4-6 | 5 | 0.166 | 5.28 | 0.0108 |
| haiku-5-5 | 4 | 0.073 | 42.86 | 1.0000 |
| sonnet-5-5 | 5 | 0.046 | 0.00 | 0.5000 |
| opus-5-5 | 5 | 0.009 | 0.37 | 0.7276 |

## E5. Override by template (included cells pooled)

| template | override |
|---|---|
| T1_detector | 73/340 (0.215) |
| T2_instrument | 77/340 (0.226) |
| T3_review | 79/340 (0.232) |
| T4_proposal | 85/340 (0.250) |
| T5_plain | 73/340 (0.215) |

## E6. Leave-one-unit-out H2 (LR test of model effect)

| left out | LR | df | p |
|---|---|---|---|
| p01_xenon1t | 330.3 | 6 | 2.7e-68 |
| p02_gerda | 253.3 | 6 | 7.9e-52 |
| p03_advirgo | 142.5 | 6 | 3e-28 |
| p05_sno | 182.7 | 6 | 9e-37 |
| p09_nemo3 | 327.3 | 6 | 1.2e-67 |
