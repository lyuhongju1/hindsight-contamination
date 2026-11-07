# Negative control NC1 (p09_nemo3; single unit, NC-A1)

Included models (K-correct on CONF1 and NC_CONF; NC K gate PASS): 7

| model | B_adopted (BASE P) | O_adopted (CONF1 override) | B_alt (NC_BASE ALT) | O_alt (NC_CONF override) |
|---|---|---|---|---|
| claude-sonnet-4-5-20250929 | 0/50 | 0/50 | 0/50 | 0/50 |
| claude-haiku-4-5-20251001 | 0/50 | 0/50 | 0/50 | 0/50 |
| claude-opus-4-5-20251101 | 0/50 | 1/50 | 0/50 | 0/50 |
| claude-sonnet-4-6 | 0/50 | 0/50 | 0/50 | 0/50 |
| claude-haiku-5-5 | 0/50 | 0/50 | 0/50 | 0/50 |
| claude-sonnet-5-5 | 10/50 | 8/50 | 2/50 | 1/50 |
| claude-opus-5-5 | 32/50 | 0/50 | 21/50 | 0/50 |

**H_NC (historical > 0):** coefficient -0.035 (SE 1.119), z = -0.03, one-sided p = 0.5125; logit(B_target) coefficient 1.604 (SE 0.488). Responses: 700; overrides: 10.
Note: if one arm has zero overrides, quasi-separation inflates the SE; the result is then reported descriptively.
