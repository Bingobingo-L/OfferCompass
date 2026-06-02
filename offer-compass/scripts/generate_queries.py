#!/usr/bin/env python3
"""Generate search queries for graduate offer research."""

from __future__ import annotations

import argparse
import json


VC_FUNDS = [
    "Sequoia",
    "HongShan",
    "a16z",
    "Lightspeed",
    "Accel",
    "Benchmark",
    "General Catalyst",
    "Index Ventures",
    "NEA",
    "Coatue",
]


def generate(company: str, role: str = "", department: str = "", founder: str = "") -> dict:
    cn = [
        f'"{company}" 融资',
        f'"{company}" 最近一轮融资',
        f'"{company}" 投资方',
        f'"{company}" 创始人',
        f'"{company}" CEO',
        f'"{company}" 客户案例',
        f'"{company}" 商业化',
        f'"{company}" 裁员',
        f'"{company}" 拖欠工资',
        f'"{company}" 劳动仲裁',
        f'"{company}" 被执行',
        f'"{company}" 期权',
        f'"{company}" 面经',
        f'"{company}" 加班',
    ]
    en = [
        f'"{company}" funding',
        f'"{company}" seed round',
        f'"{company}" Series A',
        f'"{company}" Series B',
        f'"{company}" investors',
        f'"{company}" founder',
        f'"{company}" layoffs',
        f'"{company}" revenue',
        f'"{company}" customers',
        f'site:linkedin.com/company "{company}"',
    ]
    vc = [f'"{company}" "{fund}" funding' for fund in VC_FUNDS]
    vc.extend(
        [
            f'site:sequoiacap.com "{company}"',
            f'site:a16z.com/portfolio "{company}"',
            f'site:lsvp.com/companies "{company}"',
            f'site:crunchbase.com/organization "{company}"',
        ]
    )
    role_queries = []
    if role:
        role_queries.extend(
            [
                f'"{company}" "{role}" JD',
                f'"{company}" "{role}" 面经',
                f'"{company}" "{role}" 加班',
                f'"{company}" "{role}" 绩效',
                f'site:nowcoder.com "{company}" "{role}"',
            ]
        )
    if department:
        role_queries.extend(
            [
                f'"{company}" "{department}" 裁员',
                f'"{company}" "{department}" 组织调整',
                f'"{company}" "{department}" 校招',
                f'site:linkedin.com/in "{company}" "{department}"',
            ]
        )
    if founder:
        en.extend(
            [
                f'"{founder}" "{company}"',
                f'site:x.com "{founder}" "{company}"',
                f'site:linkedin.com/in "{founder}" "{company}"',
            ]
        )

    return {
        "company_cn": cn,
        "company_en": en,
        "vc_and_funding": vc,
        "role_department": role_queries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("company")
    parser.add_argument("--role", default="")
    parser.add_argument("--department", default="")
    parser.add_argument("--founder", default="")
    args = parser.parse_args()
    print(json.dumps(generate(args.company, args.role, args.department, args.founder), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
