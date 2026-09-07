# ═══════════════════════════════════════════════════════
# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Topics: Array, Two Pointers, Binary Search
# Runtime: 3 ms (Beats 79.6%)
# Memory: 20.7 MB (Beats 8.5%)
# Submitted: Sep 7, 2026
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# ═══════════════════════════════════════════════════════

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            sumi=numbers[i]+numbers[j]
            if sumi==target:
                return [i+1,j+1]
            elif sumi<target:
                i+=1
            else:
                j-=1
        return [-1,-1]
        
