class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            odd_case = self.palindrome(s, i, i)
            even_case = self.palindrome(s, i, i + 1)
            if len(odd_case) > len(result):
                result = odd_case
            if len(even_case) > len(result):
                result = even_case
        return result
        
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]