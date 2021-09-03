class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        result[0] = 1
        for i in range(0, len(nums) - 1, 1):
            result[i + 1] = result[i] * nums[i]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= tmp
            tmp *= nums[i]
        return result
        