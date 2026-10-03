# ═══════════════════════════════════════════════════════
# Problem: 175. Combine Two Tables
# Difficulty: Easy
# Topics: Database
# Runtime: 283 ms (Beats 51.3%)
# Memory: 68.7 MB (Beats 33.2%)
# Submitted: Oct 3, 2026
# Link: https://leetcode.com/problems/combine-two-tables/
# ═══════════════════════════════════════════════════════

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    li = pd.merge(person, address, on='personId', how='left')
    return li[['firstName', 'lastName', 'city', 'state']]
