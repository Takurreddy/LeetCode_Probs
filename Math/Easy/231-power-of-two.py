# ═══════════════════════════════════════════════════════
# Problem: 231. Power of Two
# Difficulty: Easy
# Topics: Math, Bit Manipulation, Recursion
# Runtime: 2 ms (Beats 16.1%)
# Memory: 19.7 MB (Beats 5.8%)
# Submitted: Oct 10, 2026
# Link: https://leetcode.com/problems/power-of-two/
# ═══════════════════════════════════════════════════════

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and math.log2(n) % 1 == 0:
            return True
        return False
