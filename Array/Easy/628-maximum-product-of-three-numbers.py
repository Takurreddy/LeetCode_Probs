# ═══════════════════════════════════════════════════════
# Problem: 628. Maximum Product of Three Numbers
# Difficulty: Easy
# Topics: Array, Math, Sorting
# Runtime: 22 ms (Beats 42.6%)
# Memory: 20.3 MB (Beats 80.6%)
# Submitted: Oct 3, 2026
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
# ═══════════════════════════════════════════════════════

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        val=nums[n-1]*nums[n-2]*nums[n-3]
        cal=nums[0]*nums[1]*nums[n-1]
        res=max(cal,val)
        return res
