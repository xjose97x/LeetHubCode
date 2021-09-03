class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, n in enumerate(nums):
            needed = target - n
            if needed in seen:
                return [seen[needed], index]
            seen[n] = index