# ═══════════════════════════════════════════════════════
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Topics: Array, Two Pointers, Greedy
# Runtime: 60 ms (Beats 39.0%)
# Memory: 29.7 MB (Beats 38.4%)
# Submitted: Sep 7, 2026
# Link: https://leetcode.com/problems/container-with-most-water/
# ═══════════════════════════════════════════════════════

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxi=0
        while left<right:
            h=min(height[left],height[right])
            width=right-left
            area=h*width
            maxi=max(maxi,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
