# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if not head or not head.next:
            return head
        
        l = head
        mid = self.getMid(head)
        r = mid.next
        mid.next = None

        # recursion relation

        left = self.sortList(l)
        right = self.sortList(r)

        return self.merge(left,right)
        

    def getMid(self,head):
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        
        return slow


    def merge(self,left_half,right_half):

        dummy = ListNode()

        tail = dummy

        while left_half and right_half:

            if left_half.val < right_half.val:
                tail.next = left_half
                left_half = left_half.next
            else:
                tail.next = right_half
                right_half = right_half.next
            tail = tail.next
        tail.next = left_half or right_half
        return dummy.next 