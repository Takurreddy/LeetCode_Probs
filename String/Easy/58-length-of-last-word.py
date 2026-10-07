# ═══════════════════════════════════════════════════════
# Problem: 58. Length of Last Word
# Difficulty: Easy
# Topics: String
# Runtime: 0 ms (Beats 100.0%)
# Memory: 19.2 MB (Beats 54.7%)
# Submitted: Oct 7, 2026
# Link: https://leetcode.com/problems/length-of-last-word/
# ═══════════════════════════════════════════════════════

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ch=s.strip()[::-1]
        c=0
        for i in ch:
            if i==' ':
                return c
            else :
                c+=1
        return c

