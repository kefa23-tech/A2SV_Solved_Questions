# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        
        second.next = first
        
        return second
            
        # dummy = ListNode(0,head)
        
#         prev,curr = dummy,head
        
#         while curr and curr.next:
            
#             nxtpair = curr.next.next
#             second = curr.next
            
#             second.next = curr
            
#             curr.next = nxtpair
            
#             prev.next = second
            
#             prev = curr
#             curr = nxtpair
#         return dummy.next
            
    