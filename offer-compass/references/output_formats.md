# Output Formats

## Purpose

Stabilize delivery. The user should receive a clear recommendation, not a loose pile of analysis.

## Default Principles

```text
recommendation first
ranking before details
evidence and confidence for important claims
information gaps become risk and confidence language
scores are approximate aids
do not send the user away to collect information as the main conclusion
```

Exception: before the first analysis, if the required objective minimum input is missing, ask for it instead of giving a recommendation.

Required objective minimum:

```text
candidate background
company and role name for each offer
compensation structure for each offer
```

## Quick Decision

Use when the user wants a fast answer.

```text
推荐排序：
1. Offer A
2. Offer B

一句话结论：
...

关键原因：
- ...
- ...
- ...

最大风险：
...

置信度：
高 / 中 / 低
```

## Full Analysis

Default for serious offer comparison:

```text
1. Final ranking
2. One-sentence recommendation
3. Personal risk-budget summary
4. Offer-by-offer research cards
5. Company quality judgment
6. Role and team value judgment
7. Compensation and equity judgment
8. Long-term career value
9. Risk scenarios
10. Why the top offer wins
11. Why others are not preferred
12. Confidence and what could change the conclusion
```

## Comparison Matrix

For multiple offers:

```text
| Dimension | Offer A | Offer B | Offer C |
|---|---|---|---|
| Company quality | High | Medium | Low |
| Role core level | Medium | High | Low |
| Training value | High | Medium | Low |
| Guaranteed cash | High | Medium | High |
| Uncertain upside | Low | High | Medium |
| Information visibility | High | Low | Medium |
| Downside risk | Low | High | Medium |
| Long-term value | High | High | Medium |
| Recommendation | Recommend | Conditional | Not Preferred |
```

## Evidence Format

For important judgments:

```text
判断：
证据：
置信度：
影响：
```

Example:

```text
判断：B 公司融资和客户信息可见度偏低。
证据：公开搜索主要集中在官网和招聘信息，缺少权威融资报道和客户案例。
置信度：中。
影响：降低公司质量评分，提高初创风险折扣。
```

## Confidence Language

```text
High: multiple high-confidence sources agree
Medium: credible sources exist but some key details remain unverified
Low: mostly company-controlled or low-confidence sources
```

Even with low confidence, give a current-evidence recommendation.
