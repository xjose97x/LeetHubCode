class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second