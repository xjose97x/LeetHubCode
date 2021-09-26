from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for n in nums:
            if not n in dictionary:
                dictionary[n] = 0
            dictionary[n] += 1
        
        heap = PriorityQueue()

        for key, value in dictionary.items():
            heap.put((-value, key))
        result = []
        while k:
            result.append(heap.get()[1])
            k -= 1
        return result
        