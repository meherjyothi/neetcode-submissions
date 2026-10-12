# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find mid, let first half be lnger (my choice but other params will change acc if not)
        slow, fast = head, head 
        while fast and fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        #slow now is mid 

  
        #reverse w slow.next(so 1st half longer if odd) as head of list 2
        curr = slow.next 
        prev = slow.next = None
        
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt
        # reversed from prev

        #merge 
        first, second = head, prev

        #******* otherwise have to cut it etc etc   
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2 


        
        