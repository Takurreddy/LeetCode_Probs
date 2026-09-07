# ═══════════════════════════════════════════════════════
# Problem: 1019. Squares of a Sorted Array
# Difficulty: Easy
# Topics: Array, Two Pointers, Sorting
# Runtime: 7 ms (Beats 78.3%)
# Memory: 20.8 MB (Beats 82.9%)
# Submitted: Sep 7, 2026
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# ═══════════════════════════════════════════════════════

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]        
        nums=sorted(nums)
        return nums 
