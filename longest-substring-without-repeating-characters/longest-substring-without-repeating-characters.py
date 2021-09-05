class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        runner = ''
        for char in s:
            if char in runner:
                runner = runner[runner.index(char) + 1:]
            runner += char
            res = max(res, len(runner))
        return res