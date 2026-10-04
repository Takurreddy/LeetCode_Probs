# ═══════════════════════════════════════════════════════
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Topics: Array, Hash Table, String, Sorting
# Runtime: 7 ms (Beats 98.3%)
# Memory: 22 MB (Beats 65.3%)
# Submitted: Oct 4, 2026
# Link: https://leetcode.com/problems/group-anagrams/
# ═══════════════════════════════════════════════════════

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for word in strs :
            key="".join(sorted(word))
            if key not in freq:
                freq[key]=[]
            freq[key].append(word)
        for key,value in freq.items():
            return list(freq.values())
