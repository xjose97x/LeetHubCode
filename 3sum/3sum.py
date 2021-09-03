class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                values = [nums[i], nums[j], nums[k]]
                sum_values = sum(values)
                if sum_values > 0:
                    k -= 1
                elif sum_values < 0:
                    j += 1
                else:
                    result.append(values)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
        return result