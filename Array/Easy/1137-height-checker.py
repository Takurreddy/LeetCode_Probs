# ═══════════════════════════════════════════════════════
# Problem: 1137. Height Checker
# Difficulty: Easy
# Topics: Array, Sorting, Counting Sort, Bubble Sort
# Runtime: 0 ms (Beats 100.0%)
# Memory: 19.4 MB (Beats 17.2%)
# Submitted: Sep 7, 2026
# Link: https://leetcode.com/problems/height-checker/
# ═══════════════════════════════════════════════════════

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp=[]
        c=0
        exp=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=exp[i]:
                c+=1
        return c
