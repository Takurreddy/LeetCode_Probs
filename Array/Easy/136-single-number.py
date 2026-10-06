# ═══════════════════════════════════════════════════════
# Problem: 136. Single Number
# Difficulty: Easy
# Topics: Array, Bit Manipulation
# Runtime: 7 ms (Beats 29.5%)
# Memory: 21.5 MB (Beats 19.5%)
# Submitted: Oct 6, 2026
# Link: https://leetcode.com/problems/single-number/
# ═══════════════════════════════════════════════════════

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for value in freq:
            if freq[value]==1:
                return value
