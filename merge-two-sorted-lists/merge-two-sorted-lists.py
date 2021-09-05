# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        runner = result
        while l1 or l2:
            l1_val = l1.val if l1 else l2.val + 1
            l2_val = l2.val if l2 else l1.val + 1
            if l1_val < l2_val:
                runner.next = l1
                l1 = l1.next
            else:
                runner.next = l2
                l2 = l2.next
            runner = runner.next
        return result.next