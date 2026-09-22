# ═══════════════════════════════════════════════════════
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Topics: Array, Hash Table, Union-Find
# Runtime: 44 ms (Beats 77.7%)
# Memory: 36.4 MB (Beats 87.0%)
# Submitted: Sep 22, 2026
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# ═══════════════════════════════════════════════════════

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        nums=sorted(nums)
        best=1
        c=1
        if len(nums)<1:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                c+=1
                best=max(c,best)
            else:
                c=1
        return best

