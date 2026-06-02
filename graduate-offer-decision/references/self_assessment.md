# Self Assessment

## Purpose

Build a personal risk-budget model. Do not run a personality test.

The goal is to understand:

```text
Where is the candidate constrained?
What can support the candidate if the first job goes wrong?
How much platform signal, cash certainty, and structured training does the candidate need?
```

## Strong Decision Inputs

### Hard Constraints

Evaluate constraints that can override normal preference:

```text
cash floor
city rigidity
hukou or visa need
family responsibility
health and schedule limits
```

Use 0-3 levels:

```text
0 = no constraint
1 = preference
2 = important constraint
3 = decisive constraint
```

Rules:

- If hukou, visa, or family cash flow is level 3, high-risk offers should be heavily discounted.
- If health or schedule limits are high, offers with unstable nights/weekends should be penalized.
- City constraints affect both job quality and future mobility.

### Support Capacity

Merge family safety net and job-search volatility tolerance into support capacity.

Observable inputs:

```text
runway_months = available savings and explicit support / monthly necessary spending
family acceptance of career volatility
resume support for a second job search
psychological recovery capacity after layoff or failed probation
```

Rough thresholds:

```text
<3 months: avoid high-risk startups
3-6 months: consider only mature or cash-reliable startups
6-12 months: can consider growth-stage startups if role and company quality are strong
12+ months: has realistic room to try earlier-stage opportunities
```

### Campus Window Value

New-grad status is an asset. Evaluate:

```text
rarity of the big-company or core-role offer
difficulty of entering a similar platform later through social hiring
first-company resume signal
whether the offer is an entry ticket to a high-barrier sector such as AI infra, chip, quant, robotics, or global SaaS
```

If the candidate lacks brand signal, a strong first platform has higher value.

### Calibration Experience

Judge whether the candidate has real environment feel:

```text
0 = no real organization or high-intensity experience
1 = ordinary internship or project
2 = real big-company or startup experience
3 = both environments experienced and differences can be described
```

Low calibration does not forbid startup choice, but it lowers confidence and increases the risk penalty for low-visibility offers.

### Self-Directed Execution

Use behavior evidence, not self-description:

```text
independently found internship, project, mentor, or opportunity
self-learned a skill and produced visible work
contacted strangers to get information or resources
advanced a task without clear assignment
turned an ambiguous problem into a plan and executed it
```

Score 0-5:

```text
0-1: depends more on mature organizations and explicit training
2-3: can consider mature startup or core big-company team
4-5: has basic fit for exploratory environments
```

### Relationship And Upward Management

Especially important for startups and ambiguous teams.

Evidence:

```text
can ask clarifying questions
can push back respectfully
can request resources and feedback
can handle conflict without freezing
has been a coordinator in team work
others are willing to work with the candidate again
```

Score:

```text
0 = avoids conflict, waits to be arranged
1 = communicates normally but rarely claims resources
2 = can coordinate, escalate, and manage upward
```

### Cash Certainty Need

Do not ask "do you care about money?" Everyone does.

Ask or infer:

```text
minimum annual cash need
debt, rent, family transfer, or tuition pressure
acceptable base-vs-equity tradeoff
whether options going to zero is acceptable
```

This links to compensation analysis.

### Long-Term Direction Clarity

Evaluate whether the candidate knows what capabilities they want in 2-3 years:

```text
technical expert
product or business owner
research
sales or customer-facing
management
founder path
high-income stable professional
```

Low clarity increases the value of structured training and broad platform signal. High clarity can increase the value of a highly relevant core role.

## Weak Signals

Use only if provided; do not require them:

```text
GPA
competitions
papers
open source
brand-name internships
strong referrers
prestigious school
English ability
```

These are useful for estimating repair capacity and market signal, but they do not directly decide startup vs big company.

## Excluded Signals

Do not use MBTI, zodiac signs, or personality labels as formal evidence. They may inspire follow-up hypotheses, but never conclusions.

Growth history can be used cautiously as a hypothesis source:

```text
small city to top university
low-resource background to competitive environment
recovered from failure
long-term independent opportunity seeking
```

Treat these as hypotheses to cross-check, not labels.

## Output

Produce:

```text
hard_constraints_score:
support_capacity_score:
campus_window_value:
calibration_score:
agency_score:
relationship_score:
cash_certainty_need:
path_clarity_score:
personal_risk_budget:
decision_implications:
```
