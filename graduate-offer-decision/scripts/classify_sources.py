#!/usr/bin/env python3
"""Classify source URLs into rough evidence tiers."""

from __future__ import annotations

import argparse
import json
from urllib.parse import urlparse


HIGH_DOMAINS = {
    "sec.gov": "filing",
    "hkexnews.hk": "filing",
    "cninfo.com.cn": "filing",
    "gsxt.gov.cn": "government_registry",
    "court.gov.cn": "legal",
    "sequoiacap.com": "vc_site",
    "a16z.com": "vc_site",
    "lsvp.com": "vc_site",
}

MEDIUM_DOMAINS = {
    "36kr.com": "media",
    "latepost.com": "media",
    "huxiu.com": "media",
    "tmtpost.com": "media",
    "jiemian.com": "media",
    "caixin.com": "media",
    "crunchbase.com": "company_database",
    "linkedin.com": "employee_profile",
    "github.com": "technical_signal",
    "zhipin.com": "job_board",
    "lagou.com": "job_board",
    "liepin.com": "job_board",
    "nowcoder.com": "interview_signal",
}

LOW_DOMAINS = {
    "maimai.cn": "anonymous_or_workplace_signal",
    "kanzhun.com": "review_signal",
    "zhihu.com": "social_signal",
    "xiaohongshu.com": "social_signal",
    "x.com": "social_signal",
    "twitter.com": "social_signal",
    "reddit.com": "forum_signal",
}


def classify(url: str) -> dict:
    host = urlparse(url).netloc.lower().removeprefix("www.")
    for domain, source_type in HIGH_DOMAINS.items():
        if host.endswith(domain):
            return {"url": url, "tier": "high", "source_type": source_type}
    for domain, source_type in MEDIUM_DOMAINS.items():
        if host.endswith(domain):
            return {"url": url, "tier": "medium", "source_type": source_type}
    for domain, source_type in LOW_DOMAINS.items():
        if host.endswith(domain):
            return {"url": url, "tier": "low", "source_type": source_type}
    return {"url": url, "tier": "unknown", "source_type": "unclassified"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+")
    args = parser.parse_args()
    print(json.dumps([classify(url) for url in args.urls], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
