# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2Lists(l1, l2):
            dummy = ListNode()
            c = dummy
            c1, c2 = l1, l2
            while c1 and c2:
                if c1.val<=c2.val:
                    c.next = c1
                    c1 = c1.next
                else:
                    c.next = c2
                    c2 = c2.next 
                c = c.next 
            c.next = c1 or c2 

            return dummy.next 
        
        if len(lists)==0:
            return None
        
        while len(lists) > 1:

            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merged.append(merge2Lists(l1, l2))
            lists = merged


        return lists[0]

        