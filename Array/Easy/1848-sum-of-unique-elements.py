# ═══════════════════════════════════════════════════════
# Problem: 1848. Sum of Unique Elements
# Difficulty: Easy
# Topics: Array, Hash Table, Counting
# Runtime: 0 ms (Beats 100.0%)
# Memory: 19.4 MB (Beats 21.0%)
# Submitted: Oct 3, 2026
# Link: https://leetcode.com/problems/sum-of-unique-elements/
# ═══════════════════════════════════════════════════════

from collections import Counter 
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        '''
        n=len(nums)
        stack=[0]*n
        for i in range(len(nums)):
            if nums[i] not in stack:
                stack[i]=nums[i]
            else:
                stack[i].remove(nums[i])
        sume=0
        sume=sum(stack)
        return sume
        '''
        s=0
        counts=Counter(nums)
        for i in nums:
            if counts[i]==1:
                s+=i
        return s
