class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = -1
        right = 0
        seen = {}
        while right < len(s):
            char = s[right]
            if char in seen:
                left = max(left, seen[char])
            seen[char] = right
            result = max(result, right - left)
            right += 1
        
        return result