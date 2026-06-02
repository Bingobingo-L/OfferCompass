# Compensation And Equity

## Purpose

Do not compare headline total compensation. Compare:

```text
risk-adjusted value
cash certainty
downside protection
equity credibility
hidden terms
```

## Components

Guaranteed cash:

```text
base
fixed allowance
guaranteed signing bonus
guaranteed relocation or settlement allowance
```

Semi-guaranteed value:

```text
year-end bonus
performance bonus
project bonus
company-performance-linked pay
```

High-uncertainty value:

```text
startup options
unlisted shares
oral raise promise
future financing adjustment
```

Do not simply add these together.

## Cash Certainty

Compute if possible:

```text
annual_guaranteed_cash = base * pay_months + guaranteed_bonus + first_year_signing_bonus
cash_coverage_ratio = annual_guaranteed_cash / personal_minimum_cash_need
```

Interpretation:

```text
<1.0: dangerous
1.0-1.3: barely covered
1.3-1.8: relatively safe
>1.8: lower cash pressure
```

If cash coverage is low and equity is vague, heavily penalize the offer.

## Bonus

Check:

```text
written in offer or verbal
guaranteed or performance-based
individual or company-performance linked
historical payout stability
company growth or contraction signal
```

Verbal bonus promises should be discounted heavily.

## RSU Versus Options

RSU:

```text
usually from listed or mature companies
easier to estimate
has vesting schedule
market-price risk
more liquid than startup options
```

Options:

```text
right to buy shares at strike price
value depends on exit, IPO, acquisition, or buyback
affected by strike price, taxes, dilution, and exercise window
often worth zero
```

Big-company RSU and startup options are not equivalent.

## Startup Option Evaluation

Important terms:

```text
grant number
fully diluted ownership percentage
strike price
current valuation
latest round valuation
vesting schedule
cliff
post-termination exercise window
early exercise
repurchase terms
dilution risk
exit path
```

Default rules:

- If percentage, strike price, vesting, and exercise window are unknown, do not count options as guaranteed value.
- If only "option package worth X" is known, treat as low-confidence high-risk upside.
- If the company is unlisted and has no liquidity path, options are upside only, not a decision base.

## Hidden Compensation And Terms

Check:

```text
social insurance and housing fund contribution base
supplemental insurance
meal, housing, transport allowance
remote or flexible work
annual leave
overtime meal and taxi
training budget
equipment
hukou or visa support
probation salary discount
non-compete
penalty clauses
```

## Risk-Adjusted Value

Use rough weights:

```text
guaranteed_cash: 1.0
guaranteed_bonus: 0.8-1.0
performance_bonus: 0.3-0.7
listed_company_RSU: 0.5-0.9
startup_options_clear_terms: 0.05-0.3
startup_options_unclear_terms: 0-0.05
oral_promises: 0
```

This is not a precise finance model. It prevents uncertain value from being treated as cash.

## Red Flags

```text
low base offset by vague options
option value without percentage or strike price
unclear vesting
bonus only verbal
minimum social-insurance base
probation salary discount with unclear assessment
salary delay reports
unreasonable non-compete
training loan, deposit, or guarantee requirement
excessive tripartite-agreement penalty
```

## Output

```text
guaranteed_cash:
semi_guaranteed_value:
uncertain_upside:
cash_coverage_ratio:
equity_confidence:
compensation_risk_level:
risk_adjusted_compensation_estimate:
red_flags:
recommendation_impact:
```
