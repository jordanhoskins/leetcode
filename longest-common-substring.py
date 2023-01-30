"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len in {0, 1}:
            return s_len
        start = 0
        end = 0
        substring = set()
        max_substring_len = 0
        while start < s_len:
            while end < s_len:
                if s[end] not in substring:
                    substring.add(s[end])
                    end += 1
                else:
                    if len(substring) > max_substring_len:
                        max_substring_len = len(substring)
                    substring = set()
                    break
            start += 1
            end = start

        return max_substring_len
