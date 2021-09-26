from queue import PriorityQueue

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heap = PriorityQueue()
        nums = set(nums)
        for n in nums:
            heap.put(n)
        
        result = 1
        runner = 1
        prev = heap.get()
        while not heap.empty():
            current = heap.get()
            if prev + 1 == current:
                runner += 1
            else:
                runner = 1
            prev = current
            result = max(result, runner)
        return result