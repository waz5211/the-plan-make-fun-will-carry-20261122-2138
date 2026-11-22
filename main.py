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


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
