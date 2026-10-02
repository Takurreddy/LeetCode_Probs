# ═══════════════════════════════════════════════════════
# Problem: 1528. Kids With the Greatest Number of Candies
# Difficulty: Easy
# Topics: Array
# Runtime: 0 ms (Beats 100.0%)
# Memory: 19.1 MB (Beats 91.7%)
# Submitted: Oct 2, 2026
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# ═══════════════════════════════════════════════════════

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n=len(candies)
        li=[0]*n
        m=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                li[i]=True
            else:
                li[i]=False
        return li
