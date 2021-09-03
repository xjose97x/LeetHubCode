class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        runner = 0
        for n in nums:
            if runner + n < 0:
                runner = 0
                result = max(result, n)
            else:
                runner += n
                result = max(result, runner)                
        return result