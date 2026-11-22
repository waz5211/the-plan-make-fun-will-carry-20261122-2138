#!/usr/bin/env python3
"""Write the competition plan to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
"""

import os

ENTRY_TEXT = (
    "Day 1: list a $25 AI product-description gig on Fiverr for Shopify "
    "pet stores: 5 descriptions in 24h, AI draft + polish. Spend $29 on "
    "an AI writing subscription and $20 promoting the gig; keep $51 float. "
    "Reinvest each sale into promotion. Target 20 orders in 30 days, "
    "about $500."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the entry text fits the 1-280 character gate.

    The entry must be 1 to 280 Unicode code points and must not be
    whitespace-only; anything else raises SystemExit with a clear message.
    """
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry text must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry text must not be whitespace-only")


def main() -> None:
    validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
