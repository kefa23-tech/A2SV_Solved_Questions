# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        nodes.sort()

        cur = head

        for val in nodes:
            cur.val = val
            cur = cur.next
        
        return head