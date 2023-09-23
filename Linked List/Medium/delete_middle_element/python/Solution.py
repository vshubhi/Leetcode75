# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
          head = None
          return head
        slow= ListNode()
        slow.next = head
        fast = head
        while fast and fast.next!=None:
          slow = slow.next
          fast = fast.next.next
        temp = slow.next
        slow.next = temp.next
        return head
    