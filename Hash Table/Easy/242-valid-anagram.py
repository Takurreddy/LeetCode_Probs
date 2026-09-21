# ═══════════════════════════════════════════════════════
# Problem: 242. Valid Anagram
# Difficulty: Easy
# Topics: Hash Table, String, Sorting
# Runtime: 19 ms (Beats 16.0%)
# Memory: 20.2 MB (Beats 21.1%)
# Submitted: Sep 21, 2026
# Link: https://leetcode.com/problems/valid-anagram/
# ═══════════════════════════════════════════════════════

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        else:
            return False
