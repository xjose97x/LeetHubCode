from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = PriorityQueue()
        
        for l in lists:
            while l:
                heap.put(l.val)
                l = l.next
        
        dummy = ListNode()
        runner = dummy
        while not heap.empty():
            runner.next = ListNode(heap.get())
            runner = runner.next
        return dummy.next