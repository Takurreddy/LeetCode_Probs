# ═══════════════════════════════════════════════════════
# Problem: 283. Move Zeroes
# Difficulty: Easy
# Topics: Array, Two Pointers
# Runtime: 5 ms (Beats 49.9%)
# Memory: 20.6 MB (Beats 25.7%)
# Submitted: Oct 5, 2026
# Link: https://leetcode.com/problems/move-zeroes/
# ═══════════════════════════════════════════════════════

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                nums.append(nums[i])
                nums.remove(nums[i])
        '''
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
