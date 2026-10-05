# ═══════════════════════════════════════════════════════
# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Topics: Two Pointers, String
# Runtime: 7 ms (Beats 80.8%)
# Memory: 19.6 MB (Beats 78.4%)
# Submitted: Oct 5, 2026
# Link: https://leetcode.com/problems/valid-palindrome/
# ═══════════════════════════════════════════════════════

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for char in s:
            if char.isalnum():
                s1 += char.lower()
        if s1==s1[::-1]:
            return True
        return False
