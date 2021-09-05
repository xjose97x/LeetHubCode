class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        left = -1
        right = 0
        while right < len(s):
            char = s[right]
            if char in seen:
                left = max(left, seen[char])
            seen[char] = right
            res = max(res, right - left)
            right += 1
        return res