"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head1: 'Optional[Node]') -> 'Optional[Node]':

        hm = {None:None}
        c1 = head1
        while c1:
            newNode = Node(c1.val)
            hm[c1] = newNode
            c1 = c1.next

        
        c1 = head1
        while c1:
            hm[c1].next = hm[c1.next]
            hm[c1].random = hm[c1.random]
            c1 = c1.next 
        
        return hm[head1]

        





        