# Risk Scenarios

## Purpose

Do not only score offers. Build realistic scenarios and judge downside, reversibility, and regret.

The question is:

```text
Which risk is worth taking, and which bad outcome can the candidate recover from?
```

## Scenario Framework

For each offer:

```text
upside_case
base_case
downside_case
```

Startup example:

```text
upside: company grows, candidate enters core project, obtains ownership
base: company survives, direction changes, candidate learns some skills and leaves after 1-2 years
downside: funding fails, layoffs happen, role is messy, candidate must job-search again
```

Big-company example:

```text
upside: core team, strong training, strong resume, promotion or later switch
base: stable job, process learning, moderate growth
downside: edge business, repeated internal work, org change, weak skill growth
```

## Downside Analysis

Classify losses:

```text
cash loss
time loss
resume loss
skill loss
psychological cost
city, hukou, or visa loss
campus-window loss
health cost
```

## Reversibility

Reversible:

```text
short-term project mismatch
slightly lower first-year pay
temporary city mismatch
technical stack mismatch
```

Semi-reversible:

```text
weak first resume signal
narrow direction for 1 year
low-quality first-job training
missing some campus opportunities
```

Hard to reverse:

```text
hukou or visa miss
cash-flow break
serious health damage
restrictive non-compete
long time away from target industry
missing rare core big-company campus offer
```

## Regret Analysis

Estimate likely regret source:

```text
startup regret: company fails, training is weak, cash is low, resume is hard to explain
big-company regret: growth is slow, role is edge, impact is small, missed upside
```

## Probability Bands

Use coarse probability:

```text
low / medium / high
low probability high impact
medium probability medium impact
high probability low impact
```

Avoid fake precision.

## Decision Rules

- If downside triggers cash break, hukou/visa failure, or health damage, do not recommend high-risk offers.
- If startup downside is recoverable and upside is materially better than big-company baseline, it can be recommended.
- If big-company baseline already provides strong training and strong resume signal, its priority is high.
- If two offers are close, prefer lower downside and better transferability.
- If a startup is attractive only in upside but weak in base/downside, do not recommend it.

## Output

```text
scenario_analysis:
  offer_name:
    upside_case:
    base_case:
    downside_case:
    downside_severity:
    reversibility:
    main_regret_risk:
    risk_compensation:
    recommendation_under_uncertainty:
```
