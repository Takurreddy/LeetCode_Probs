# ═══════════════════════════════════════════════════════
# Problem: 263. Ugly Number
# Difficulty: Easy
# Topics: Math
# Runtime: 1 ms (Beats 25.5%)
# Memory: 19.3 MB (Beats 29.7%)
# Submitted: Sep 26, 2026
# Link: https://leetcode.com/problems/ugly-number/
# ═══════════════════════════════════════════════════════

class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False 
        
        for i in (2,3,5):
            while n%i==0:
                n//=i

        return n==1

