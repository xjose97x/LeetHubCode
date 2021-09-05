class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        queue = []
        
        for c in s:
            if c in match:
                queue.append(c)
            elif not queue or match[queue.pop()] != c:
                return False
        return len(queue) == 0