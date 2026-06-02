# Decision Framework

## Purpose

Synthesize personal risk budget, research, company quality, role value, compensation, long-term value, and risk scenarios into a final offer ranking.

The output must be actionable. Do not end with "it depends" unless followed by a clear conditional recommendation.

## Inputs

```text
personal_risk_budget
hard_constraints
support_capacity
company_quality_score
company_risk_level
role_core_score
training_value_score
resume_value_score
compensation_risk_level
cash_coverage_ratio
long_term_value_score
scenario_downside_severity
information_confidence
```

## Hard Filters

Apply before scoring:

```text
cash coverage < 1.0 and support capacity weak
hukou or visa constraint decisive and unsupported
startup information visibility extremely low
role vague and cannot be externally verified
salary delay, legal, or severe layoff signal
big-company business line clearly shrinking and role is edge
unreasonable non-compete or penalty clauses
```

Hard filters do not always mean "avoid", but they force a conservative ranking.

## Scoring Aid

Use 100-point scoring only as a thinking aid:

```text
final_score =
  personal_fit * 20
  + company_quality * 20
  + role_training_value * 20
  + compensation_quality * 15
  + long_term_value * 15
  + downside_resilience * 10
  - risk_penalties
```

Do not present the score as exact science.

## Weight Adjustments

```text
cash pressure high -> weight compensation certainty and downside control higher
weak platform signal -> weight resume signal higher
strong support capacity -> allow more long-term upside risk
low internship calibration -> penalize low-visibility offers more
city / hukou / visa hard constraint -> override normal ranking if necessary
startup options large but unclear -> lower compensation quality
```

## Offer Archetypes

Classify each offer:

```text
high-certainty growth: core big-company role or mature company core team, cash stable, training strong
high-risk high-upside: startup core role with strong business but meaningful downside
stable but limited-growth: mature company or big company edge role with weak training
narrative high-risk: AI story, low visibility, vague role, option-heavy package
low value: average pay, edge role, company risk, weak growth
```

## Tie Breakers

If offers are close:

```text
prefer lower downside
prefer transferable skills
prefer clearer resume story
prefer stronger direct team
prefer sufficient cash plus decent growth
avoid choosing only because of option story
avoid choosing only because of famous brand
```

## Recommendation Labels

```text
Strong Recommend
Recommend
Conditional Recommend
Conservative Pick
Upside Pick
Not Preferred
Avoid
```

## Output

```text
final_recommendation:
  ranking:
  best_choice:
  reason:
  offer_cards:
    - offer:
      archetype:
      score_or_relative_level:
      strongest_points:
      biggest_risks:
      downside:
      confidence:
  decision_logic:
    why_top_offer_wins:
    why_not_others:
    what_matters_most:
    conclusion_under_uncertainty:
```
