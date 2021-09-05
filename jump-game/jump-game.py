class Solution:
    def canJump(self, nums: List[int]) -> bool:
        required_pos = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= required_pos:
                required_pos = i
        return required_pos == 0