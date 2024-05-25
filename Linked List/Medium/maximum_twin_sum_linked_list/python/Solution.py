
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        temp = head
        while prev:
            max_sum = max(max_sum, prev.val+temp.val)
            temp = temp.next
            prev = prev.next
        return max_sum
        