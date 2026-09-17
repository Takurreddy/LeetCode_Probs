# ═══════════════════════════════════════════════════════
# Problem: 27. Remove Element
# Difficulty: Easy
# Topics: Array, Two Pointers
# Runtime: 0 ms (Beats 100.0%)
# Memory: 19.4 MB (Beats 19.4%)
# Submitted: Sep 17, 2026
# Link: https://leetcode.com/problems/remove-element/
# ═══════════════════════════════════════════════════════

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]==val:
                nums[left]=nums[right]
                right-=1
            else:
                left+=1
        return left
                
