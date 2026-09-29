# ═══════════════════════════════════════════════════════
# Problem: 2714. Left and Right Sum Differences
# Difficulty: Easy
# Topics: Array, Prefix Sum
# Runtime: 7 ms (Beats 28.2%)
# Memory: 19.5 MB (Beats 25.1%)
# Submitted: Sep 29, 2026
# Link: https://leetcode.com/problems/left-and-right-sum-differences/
# ═══════════════════════════════════════════════════════

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        li=[0]*n
        total=sum(nums)
        rightsum=[0]*n
        rightsum[0]=total-nums[0]
        prefixsum=[0]*n
        prefixsum[0]=0
        for i in range(1,n):
            prefixsum[i]=prefixsum[i-1]+nums[i-1]
        for i in range(1,n):
            rightsum[i]=total-prefixsum[i]-nums[i]
        for i in range(n):
            li[i]=abs(prefixsum[i]-rightsum[i])
        return li
