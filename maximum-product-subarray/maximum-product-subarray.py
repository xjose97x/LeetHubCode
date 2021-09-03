class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currentMax = 1
        currentMin = 1
        for n in nums:
            tmp = currentMax * n
            currentMax = max(tmp, currentMin * n, n)
            currentMin = min(tmp, currentMin * n, n)
            result = max(result, currentMax)
        return result