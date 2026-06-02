#!/usr/bin/env python3
"""Create an empty research-pack JSON skeleton."""

from __future__ import annotations

import argparse
import json


def build(company: str, role: str = "", compensation: str = "") -> dict:
    return {
        "user_input": {
            "company_name": company,
            "role_title": role,
            "compensation_structure": compensation,
        },
        "normalized_identity": {},
        "company_facts": [],
        "role_facts": [],
        "funding_facts": [],
        "founder_facts": [],
        "hiring_signals": [],
        "compensation_facts": [],
        "risk_signals": [],
        "source_map": [],
        "confidence_by_claim": [],
        "information_visibility_score": None,
        "overall_confidence": None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("company")
    parser.add_argument("--role", default="")
    parser.add_argument("--compensation", default="")
    args = parser.parse_args()
    print(json.dumps(build(args.company, args.role, args.compensation), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
