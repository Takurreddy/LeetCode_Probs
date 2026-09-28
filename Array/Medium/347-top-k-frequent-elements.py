# ═══════════════════════════════════════════════════════
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
# Runtime: 11 ms (Beats 24.7%)
# Memory: 24.7 MB (Beats 26.3%)
# Submitted: Sep 28, 2026
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# ═══════════════════════════════════════════════════════

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        lst=[[] for i in range(len(nums)+1)]
        for key,value in freq.items():
            lst[value].append(key)
        res=[]
        for i in range(len(nums),0,-1):
            for num in lst[i]:
                res.append(num)
        return res[:k]
