# ═══════════════════════════════════════════════════════
# Problem: 268. Missing Number
# Difficulty: Easy
# Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
# Runtime: 1413 ms (Beats 5.0%)
# Memory: 20.3 MB (Beats 76.2%)
# Submitted: Sep 21, 2026
# Link: https://leetcode.com/problems/missing-number/
# ═══════════════════════════════════════════════════════

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
                return i 
