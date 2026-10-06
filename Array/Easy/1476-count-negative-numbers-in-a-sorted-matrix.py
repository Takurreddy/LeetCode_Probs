# ═══════════════════════════════════════════════════════
# Problem: 1476. Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Topics: Array, Binary Search, Matrix
# Runtime: 3 ms (Beats 27.8%)
# Memory: 32.7 MB (Beats 15.5%)
# Submitted: Oct 6, 2026
# Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# ═══════════════════════════════════════════════════════

import numpy as np
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        arr=np.array(grid)
        cnt=(arr<0).sum()
        return int(cnt)
