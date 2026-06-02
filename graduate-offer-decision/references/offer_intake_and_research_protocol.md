# Offer Intake And Research Protocol

## Purpose

Turn minimal user input into a complete research task.

The user must provide three categories of objective input before full analysis starts:

```text
candidate_background
company_and_role_name
compensation_structure
```

Everything else should be researched, inferred, and confidence-labeled by the agent.

If any of these three categories is missing in the first user message, ask a concise follow-up and do not start the full comparison yet.

Do not ask subjective questions first. The first follow-up should collect only missing objective inputs.

Minimum closed-loop input:

```text
candidate:
  school:
  degree:
  major:
  graduation_status:
  internships_or_projects if provided:

offers:
  - company_name:
    role_title:
    department_or_business_line if known:
    location if known:
    compensation_structure:
```

## Normalize User Input

Create an offer card:

```text
offer_id:
company_name:
company_aliases:
possible_legal_entity:
role_title:
city_or_location:
compensation_structure:
offer_certainty:
```

If the company has multiple names, products, legal entities, or Chinese/English variants, capture them all.

## Research Targets

For each offer, build a research pack with:

```text
company identity
business model
product reality
customer or user evidence
founder and leadership background
financing or listing status
investor confirmation
headcount and hiring signal
negative news and legal risk
department or business-line signal
similar role JDs
interview and role-experience signals
employee public profiles
compensation market signal
```

## Claims And Evidence

Every important claim should be stored as:

```text
claim:
source:
source_type:
date:
confidence: high | medium | low
cross_verified: yes | no
decision_impact:
```

## Unknowns

Do not ask the user to collect unknowns as the main workflow.

Classify unknowns:

```text
decision-critical but unverifiable
moderately important
minor
```

Then convert them into:

```text
lower confidence
lower information_visibility_score
higher risk penalty
more conservative recommendation
```

## Output

For each offer:

```text
research_pack:
  user_input:
  normalized_identity:
  company_facts:
  role_facts:
  funding_facts:
  founder_facts:
  hiring_signals:
  compensation_facts:
  risk_signals:
  source_map:
  confidence_by_claim:
  information_visibility_score:
```
