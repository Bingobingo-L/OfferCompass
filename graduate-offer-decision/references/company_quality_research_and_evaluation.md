# Company Quality Research And Evaluation

## Purpose

Convert company research into a judgment about whether the company is a good first-job platform.

Company quality is not fame, valuation, or AI hype. For a new graduate, company quality means:

```text
real business
reasonable stability
credible growth
good talent environment
resume signal
capacity to train and carry new graduates
downside that can be survived
```

## Common Dimensions

Evaluate every company on:

```text
business reality
growth or contraction
cash or financing signal
organization stability
talent density
new-graduate carrying capacity
external reputation and resume signal
negative risk
information visibility
```

## Business Reality

Strong signals:

```text
real customers
paying customers
repeat usage
public product
clear use case
credible customer cases
observable revenue model
```

Weak signals:

```text
only demo
only vision
only investor story
only vague AI platform language
no visible customers
no product evidence
```

## Startup-Specific Evaluation

Evaluate:

```text
stage: seed, Series A, Series B, Series C, pre-IPO
recent financing time
runway signal
lead investors and follow investors
founder domain fit
founder execution record
product-market evidence
commercialization path
headcount growth or shrinkage
quality of early employees
option credibility
```

Rules:

- Recent financing is positive but not enough.
- Famous founders are positive but not enough.
- Paying customers are stronger than demos.
- Hiring for revenue, product, and engineering can be a growth signal.
- Heavy hiring for interns or junior execution roles can be a warning if senior density is low.
- If financing is older than 18-24 months and no revenue or follow-on signal exists, raise risk.

## Big-Company-Specific Evaluation

Evaluate:

```text
overall platform value
business-line core level
department growth or shrinkage
campus training mechanism
internal mobility
organization change risk
role edge risk
brand signal value
```

Rules:

- Big-company brand does not rescue a clearly edge, shrinking, or low-training role.
- Core business or core AI/product/infra team has much higher first-job value than internal support work.
- Strong campus training and strong peers can compensate for slower immediate impact.

## Red Flags

```text
salary delay
unpaid wages
frequent direction changes
funding gap with no revenue signal
unclear product
no verifiable customers
core employee departures
labor disputes
enforcement records
negative legal records
abnormal registry status
job descriptions that are broad but non-specific
only talks about vision, not customers or income
```

## Information Visibility

Score 0-5:

```text
5 = rich information, multiple high-confidence cross-verifications
4 = good public information, a few gaps
3 = basic information available, key business data missing
2 = mostly company-controlled information
1 = only website and hiring traces
0 = legal entity, product, financing, or team cannot be confirmed
```

Low visibility is not neutral. It increases risk.

## Output

```text
company_quality_score:
company_risk_level:
business_reality_score:
growth_signal:
cash_or_financing_signal:
organization_stability:
talent_density_signal:
new_grad_platform_value:
information_visibility_score:
confidence_level:
key_evidence:
key_risks:
```
