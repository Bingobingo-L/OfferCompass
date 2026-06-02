---
name: graduate-offer-decision
description: Use when a new graduate or early-career candidate needs to choose between startup, big company, mature company, or multiple job offers, especially in AI-era career contexts. This skill compares offers using minimal user input, active company and role research, personal risk-budget assessment, compensation certainty analysis, downside scenarios, and final recommendation ranking.
metadata:
  short-description: Help graduates choose between startup and big-company offers
---

# Graduate Offer Decision

## Goal

Help a new graduate make a grounded decision between startup, big-company, mature-company, or multiple job offers.

Do not give generic career advice. Produce a decision under uncertainty by combining:

- the candidate's personal risk budget
- the real quality of each company
- the real value of each role and team
- compensation certainty and equity risk
- long-term career value
- downside scenarios and reversibility
- evidence quality and information visibility

The default output is a clear offer ranking with reasons, risks, confidence level, and the conditions under which the recommendation would change.

## Core Principle

The user should not need to become a research analyst.

By default, require only objective minimum closed-loop information:

```text
candidate_background
company_and_role_name
compensation_structure
```

Use available search, browsing, research, and document-reading tools to actively investigate the rest.

Do not ask the user to collect company, department, role, founder, financing, or employee information as the main workflow. If information cannot be verified publicly, treat that as uncertainty: lower confidence, reduce information visibility, and increase risk penalty.

Important: if any of the three required objective inputs is missing, ask a concise follow-up before starting the full analysis. Do not begin offer comparison from incomplete first-turn input.

## When To Use

Use this skill when the user asks about:

- choosing between a startup and a big company
- comparing multiple new-grad offers
- deciding whether to join an AI startup
- evaluating a first job offer
- judging whether a company, department, or role is suitable for a new graduate
- comparing cash, RSU, options, growth, stability, and career value
- understanding whether an offer is worth taking despite uncertainty

Typical prompts:

```text
应届生应该选初创还是大厂？
帮我比较这几个 offer。
这个 AI 初创值得去吗？
大厂边缘岗和初创核心岗怎么选？
第一份工作应该更看重什么？
```

## Minimum Input

If the user has not provided the three required objective fields, ask only for the missing fields before starting the analysis.

Required field 1: candidate background.

```text
school:
degree:
major:
graduation_status:
internships_or_projects if provided:
```

Required field 2: company and role name for each offer.

```text
company_name:
role_title:
department_or_business_line if known:
location if known:
```

Required field 3: compensation structure for each offer.

```text
月薪 25k，15 薪
base 40w + bonus + 期权
总包 60w，含 RSU
薪资还没完全写清楚
```

Compensation can be rough, but the user must provide what they know. If the user only says "salary unknown", continue after recording compensation as unknown, but only if they explicitly state it is unknown.

Do not require the user to provide company background, financing details, department details, manager information, employee reviews, or market research.

Do not ask broad subjective questions in the first follow-up, such as risk preference, personality, MBTI, stress tolerance, or whether the user likes startups. Objective missing fields come first.

## Workflow

### 0. Check Required Inputs

Before research, verify:

```text
candidate_background exists
company_and_role_name exists for each offer
compensation_structure exists or is explicitly unknown for each offer
```

If any required item is missing, pause and ask for it. Keep the question short.

Example:

```text
我先需要三个客观信息再能闭环判断：
1. 你的学历背景：学校、学历、专业、是否应届；
2. 每个 offer 的公司 + 岗位/部门；
3. 每个 offer 的薪资构成。
你把缺的补一下，我再开始背调和比较。
```

### 1. Normalize Offers

Convert raw descriptions into structured offer cards:

```text
company_name
possible_legal_entity
role_title
city_or_location if provided
compensation_structure
offer_certainty if known
```

If the company name is ambiguous, use search to disambiguate by role, city, product, founder, or compensation context. Ask the user only if ambiguity cannot be reasonably resolved.

### 2. Assess Personal Risk Budget

Read `references/self_assessment.md`.

Estimate:

```text
How much risk can this candidate realistically take?
How costly would a wrong first-job choice be?
How much does this candidate need platform signal, cash certainty, or structured training?
```

Avoid pseudo-psychological conclusions. Do not rely on MBTI, zodiac signs, or personality labels as decision evidence.

### 3. Build Research Pack

Read `references/offer_intake_and_research_protocol.md` and `references/information_sources_and_research_tools.md`.

For each company and role, actively search for:

```text
company identity
legal entity
business model
products
customers or user signals
financing or listing status
founders and leadership
investors and VC confirmation
hiring signals
layoff or organization-change signals
role JD and similar roles
department or business-line signals
employee profiles
interview experiences
compensation signals
negative news, disputes, salary delays, or legal risks
```

Use source tiers and confidence rules. Treat anonymous reviews, social posts, forums, and workplace gossip as risk signals only, not facts.

If key information is missing after active research, do not stop. Record it as:

```text
unknown
low visibility
low or medium confidence
risk penalty
```

### 4. Evaluate Company Quality

Read `references/company_quality_research_and_evaluation.md`.

Judge the company as a first-job platform, not merely as a famous brand or hot startup.

Distinguish:

```text
startup: real business vs concept story; paying customers vs demo; recent financing vs stale financing
big company: brand vs actual department; core business vs edge business; training system vs internal process work
```

### 5. Evaluate Role, Team, And Training Value

Read `references/role_team_research_and_evaluation.md`.

Judge the actual role, not just the title. If role or manager information is not publicly visible, convert that into uncertainty and risk discount instead of sending the user away to collect it.

### 6. Evaluate Compensation And Equity

Read `references/compensation_and_equity.md`.

Separate compensation into:

```text
guaranteed cash
semi-guaranteed bonus
liquid or more estimable equity
high-uncertainty startup options
oral promises
benefits and hidden terms
```

Do not compare nominal total packages directly. Oral promises count as zero.

### 7. Evaluate Long-Term Career Value

Read `references/long_term_career_value.md`.

Do not predict the future. Assess whether the offer is likely to create 2-5 year career value, transferable skills, AI leverage, platform signal, and future optionality.

### 8. Build Risk Scenarios

Read `references/risk_scenarios.md`.

For each offer, produce:

```text
upside case
base case
downside case
downside severity
reversibility
main regret risk
risk compensation
```

The central question is: if this goes wrong, can the candidate recover, and is the upside large enough to justify the downside?

### 9. Make Final Decision

Read `references/decision_framework.md`.

Synthesize all prior analysis into an offer ranking. Use scoring only as an aid; do not present it as precise science.

Always produce a recommendation under current evidence. If information is incomplete, give a conservative recommendation and clearly state confidence.

## Output Rules

Read `references/output_formats.md`.

Default output should include:

```text
1. Final ranking
2. One-sentence recommendation
3. Candidate risk-budget summary
4. Offer-by-offer cards
5. Key evidence and confidence
6. Biggest risks
7. Upside/base/downside scenarios
8. Why the top offer wins
9. Why the other offers are not preferred
10. Conditions that could change the conclusion
```

For quick requests, use a shorter format:

```text
Recommended ranking
One-sentence conclusion
Top 3 reasons
Biggest risk
Confidence level
```

Do not end with "go ask HR / employees / friends and come back" as the primary answer. The skill should close the loop using available evidence.

## Reference Map

- `references/self_assessment.md`: personal risk budget, hard constraints, support capacity, cash pressure, campus-window value.
- `references/offer_intake_and_research_protocol.md`: minimal input to structured offer research.
- `references/information_sources_and_research_tools.md`: search strategy, source tiers, query templates, VC/funding search, big-company department search, startup due diligence.
- `references/company_quality_research_and_evaluation.md`: company quality, business reality, growth, financing, stability, negative signals, information visibility.
- `references/role_team_research_and_evaluation.md`: role reality, team signals, training value, resume value, role uncertainty.
- `references/compensation_and_equity.md`: guaranteed cash, bonus, RSU, startup options, benefits, hidden terms, risk-adjusted compensation.
- `references/long_term_career_value.md`: 2-5 year career value, AI-era skill compounding, platform signal, future optionality.
- `references/risk_scenarios.md`: upside/base/downside scenarios, reversibility, regret risk, downside control.
- `references/decision_framework.md`: final synthesis, hard filters, weights, archetypes, tie-breaking, recommendation labels.
- `references/output_formats.md`: final answer structure, quick/full/matrix formats, evidence display, confidence language.

## Tone And Judgment

Be direct, evidence-driven, and decision-oriented.

Avoid empty balance such as "startup has pros and cons, big company also has pros and cons." Say what matters most for this candidate under this evidence.

Do not overfit to prestige, salary, AI hype, founder charisma, or anonymous complaints.

A good answer should feel like: "I researched the offers, separated facts from uncertainty, adjusted for your personal risk budget, and here is the decision I would make under current evidence."
