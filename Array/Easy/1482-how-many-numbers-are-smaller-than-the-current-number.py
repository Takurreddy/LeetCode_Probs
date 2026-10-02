# ═══════════════════════════════════════════════════════
# Problem: 1482. How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Topics: Array, Hash Table, Sorting, Counting Sort
# Runtime: 152 ms (Beats 19.1%)
# Memory: 19.3 MB (Beats 23.6%)
# Submitted: Oct 2, 2026
# Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# ═══════════════════════════════════════════════════════

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    c+=1
            li.append(c)
        return li
