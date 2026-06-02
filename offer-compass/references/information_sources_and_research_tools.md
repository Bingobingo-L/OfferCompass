# Information Sources And Research Tools

## Purpose

This is the intelligence engine of the skill.

Search is not an auxiliary action. Without evidence, career advice is only polished guessing.

The agent must actively search, cross-verify, and classify evidence. The user should not need to collect company or role background.

## Research Loop

For every offer:

```text
1. Entity disambiguation
2. Company basic research
3. Role and department research
4. Founder and capital research
5. Risk search
6. Evidence archive and confidence labeling
```

## Source Tiers

High-confidence sources:

```text
official company website
official hiring website
government registry
exchange filings
annual reports and financial statements
SEC EDGAR
HKEXnews
CNINFO
investor official websites
court and enforcement records
patent, trademark, and software copyright databases
founder public interviews
```

Medium-confidence sources:

```text
36Kr
LatePost
Huxiu
TMTPost
Jiemian
Caixin
ChinaVenture
ITjuzi
Crunchbase
LinkedIn employee profiles
GitHub
technical blogs
papers
Boss Zhipin
Lagou
Liepin
company WeChat hiring posts
```

Low-confidence but signal-useful sources:

```text
Maimai anonymous posts
Nowcoder interview reports
Kanzhun reviews
Zhihu answers
Xiaohongshu posts
forums
X/Twitter posts
Reddit or Hacker News discussion
```

Low-confidence sources can trigger risk investigation, but cannot alone establish facts.

## Big-Company Department Search

Goal:

```text
Is the department core?
Is the business growing, shrinking, or reorganizing?
Is the role core or edge?
Can a new graduate get training and resume signal?
```

Search paths:

```text
company hiring website
annual report and public strategy material
business-line media reports
department leader interviews
LinkedIn and Maimai employee profiles
Nowcoder, Kanzhun, Maimai, Zhihu interview or workplace signals
technical blogs and conference talks
```

Query templates:

```text
"{company}" "{department}" layoff
"{company}" "{department}" organization change
"{company}" "{department}" leader
"{company}" "{department}" campus hiring
"{company}" "{role}" interview
"{company}" "{role}" JD
"{company}" "{role}" promotion
"{company}" "{business_line}" growth
"{company}" "{business_line}" shrink
"{公司名}" "{部门名}" 裁员
"{公司名}" "{部门名}" 组织调整
"{公司名}" "{岗位名}" 面经
"{公司名}" "{岗位名}" 加班
"{公司名}" "{业务线}" 收缩
site:linkedin.com/in "{company}" "{department keyword}"
site:nowcoder.com "{公司名}" "{岗位名}"
site:maimai.cn "{公司名}" "{部门名}"
```

Interpretation:

```text
Many similar JDs: possible growth signal
Long-running role with bad reviews: possible retention problem
Frequent org changes: risk up
Visible business leader and product investment: possible strategic focus
Good employee exits: resume signal up
Internal-process-only work: transferability down
```

## Startup Search

Goal:

```text
Does the company have real business, real money, real people, and a role worth taking as a first job?
```

Search paths:

```text
official website and product pages
Chinese and English company names
legal entity and registry
founder names
LinkedIn, X/Twitter, GitHub, papers, interviews
financing news
investor portfolio pages
ITjuzi, Crunchbase, ChinaVenture, 36Kr
Boss, Lagou, Liepin, official hiring pages, LinkedIn Jobs
employee profiles and exits
App Store, Android stores, Product Hunt, GitHub, API docs
court, enforcement, labor dispute, salary-delay, negative news
```

Chinese query templates:

```text
"{公司名}" 融资
"{公司名}" 完成 融资
"{公司名}" 最近一轮融资
"{公司名}" 投资方
"{公司名}" 红杉
"{公司名}" Sequoia
"{公司名}" HongShan
"{公司名}" a16z
"{公司名}" Lightspeed
"{公司名}" Crunchbase
"{公司名}" IT桔子
"{公司名}" 创始人
"{公司名}" CEO
"{公司名}" 客户案例
"{公司名}" 商业化
"{公司名}" ARR
"{公司名}" 裁员
"{公司名}" 拖欠工资
"{公司名}" 劳动仲裁
"{公司名}" 被执行
"{公司名}" 期权
"{公司名}" 面经
"{公司名}" 加班
"{公司名}" "{岗位名}" JD
```

English query templates:

```text
"{company}" funding
"{company}" seed round
"{company}" Series A
"{company}" Series B
"{company}" investors
"{company}" founder
"{company}" layoffs
"{company}" revenue
"{company}" customers
"{company}" "Sequoia"
"{company}" "a16z"
"{company}" "Lightspeed"
site:sequoiacap.com "{company}"
site:a16z.com/portfolio "{company}"
site:lsvp.com/companies "{company}"
site:crunchbase.com/organization "{company}"
site:x.com "{company}" founder
site:linkedin.com/company "{company}"
site:linkedin.com/in "{company}" founder
```

X/Twitter templates:

```text
"{company}" funding
"{company}" launch
"{company}" hiring
"{company}" layoffs
"{founder_name}" "{company}"
from:{founder_handle} funding
from:{investor_handle} "{company}"
```

X is useful for founder, investor, launch, and early user signals. Confirm with official pages, investor pages, funding reports, customer evidence, or product evidence before treating as fact.

## VC And Dollar-Fund Search

Do not only search "company + funding". Search investor portfolio pages, partner articles, podcasts, and social posts.

Important funds:

```text
Sequoia Capital
HongShan / 红杉中国
a16z
Lightspeed
Accel
Benchmark
Bessemer
Founders Fund
General Catalyst
Index Ventures
NEA
Coatue
Khosla Ventures
Greylock
Menlo Ventures
Kleiner Perkins
Peak XV
```

Templates:

```text
site:{fund_domain} "{company_english_name}"
site:{fund_domain} "{founder_name}"
"{company_english_name}" "{fund_name}" funding
"{company_english_name}" "{partner_name}"
"{company_english_name}" "{fund_name}" portfolio
"{company_english_name}" "{fund_name}" announced
```

Investor confirmation strength:

```text
investor official website > funding news > Crunchbase/ITjuzi > founder self-description > social rumor
```

Known investor participation is positive, but not sufficient. Continue checking round timing, lead vs follow, later financing, product progress, and business reality.

## Built-In Script Design

The skill may include scripts to support research, but should not depend on a single external search API.

Use:

```text
scripts/generate_queries.py
scripts/classify_sources.py
scripts/build_research_pack.py
```

Search itself should use whichever tools are available:

```text
web search
browser automation
search API
curl official pages
PDF and filing parsers
```

## Confidence Rules

```text
High:
official announcement, exchange filing, government registry, court/enforcement system, investor website, multiple credible media cross-verification.

Medium:
job posting, founder interview, investor article, LinkedIn profile, single credible media report.

Low:
anonymous review, forum post, social post, single Maimai/Zhihu/Xiaohongshu item.
```

Risk escalation:

```text
multiple low-confidence sources point to the same problem -> medium risk signal
low-confidence source plus hiring shrinkage, registry anomaly, legal record, or official negative evidence -> high risk
critical information invisible -> raise unknown risk, do not send user away to collect it
```

## Final Research Output

```text
research_summary:
  company_identity:
  legal_entity:
  business_description:
  funding_status:
  investor_quality:
  founder_quality:
  product_reality:
  customer_or_user_signal:
  hiring_signal:
  role_reality:
  department_signal:
  compensation_signal:
  risk_signals:
  information_visibility_score:
  overall_confidence:
```
