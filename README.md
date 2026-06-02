# OfferCompass

New graduate / startup vs big company offer decision.

一个用于帮助应届生和早期职业候选人比较 offer 的 Codex Skill，尤其适合判断：

- 初创公司 vs 大厂
- AI 初创 vs 成熟平台
- 大厂核心岗 vs 大厂边缘岗
- 多个产品、技术、AI 岗位 offer 的取舍

这个 Skill 的核心不是泛泛给职业建议，而是用最小客观输入启动分析，然后由 AI 主动完成公司、岗位、融资、团队、薪酬和风险背调，最后给出有证据、有置信度、有下行分析的推荐排序。

## 核心机制

第一次使用时，用户需要提供三类客观信息：

```text
1. 学历背景
   学校、学历、专业、是否应届；有实习/项目可以补充。

2. 公司 + 岗位名称
   每个 offer 的公司、岗位；如果知道部门/业务线/地点也一起给。

3. offer 薪资构成
   base、bonus、RSU/期权/股权、签字费等；不知道的可以明确说未知。
```

信息完整后，Skill 会按以下顺序运行：

```text
个人风险预算评估
offer 信息结构化
公司和岗位主动背调
公司质量评估
岗位/团队价值评估
薪资和股权风险评估
长期职业价值评估
乐观/基准/悲观情景分析
最终推荐排序
```

重要原则：

```text
用户负责提供只有用户知道的客观信息。
AI 负责搜索用户不容易查全的公开信息。
查不到的信息不甩给用户，而是转化为低置信度和风险折扣。
```

## 安装

把 `offer-compass` 目录复制到你的 Codex skills 目录：

```bash
cp -R offer-compass ~/.codex/skills/
```

然后在 Codex 中通过 `$offer-compass` 调用。

## 使用示例

```text
$offer-compass 帮我比较这两个 offer：

背景：杭州电子科技大学计算机硕士，应届。

Offer 1：
抖音 / 剪映 / AI 生图产品经理
薪资：80w 现金 + 30w RSU

Offer 2：
生数科技 / AI 产品经理
薪资：90w 现金 + 20w 股权
```

## 目录结构

```text
offer-compass/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── self_assessment.md
│   ├── offer_intake_and_research_protocol.md
│   ├── information_sources_and_research_tools.md
│   ├── company_quality_research_and_evaluation.md
│   ├── role_team_research_and_evaluation.md
│   ├── compensation_and_equity.md
│   ├── long_term_career_value.md
│   ├── risk_scenarios.md
│   ├── decision_framework.md
│   └── output_formats.md
└── scripts/
    ├── generate_queries.py
    ├── classify_sources.py
    └── build_research_pack.py
```

## 内置脚本

生成搜索 query：

```bash
python3 offer-compass/scripts/generate_queries.py "生数科技" --role "AI产品经理"
```

来源置信度分类：

```bash
python3 offer-compass/scripts/classify_sources.py https://www.sec.gov/edgar/search/
```

生成 research pack 骨架：

```bash
python3 offer-compass/scripts/build_research_pack.py "生数科技" --role "AI产品经理" --compensation "90w+20w股权"
```
