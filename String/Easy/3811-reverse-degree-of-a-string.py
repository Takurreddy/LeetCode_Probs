# ═══════════════════════════════════════════════════════
# Problem: 3811. Reverse Degree of a String
# Difficulty: Easy
# Topics: String, Simulation
# Runtime: 7 ms (Beats 74.2%)
# Memory: 19.3 MB (Beats 56.9%)
# Submitted: Oct 9, 2026
# Link: https://leetcode.com/problems/reverse-degree-of-a-string/
# ═══════════════════════════════════════════════════════

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ans += (123 - ord(c)) * (i + 1)
        return ans
