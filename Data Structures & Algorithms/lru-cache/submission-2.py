class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev, self.next = None, None 

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {} #key:nodeptr
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity 
        self.currLen = 0 

    #left, right are dummy nodes 

    #end
    def insert(self, node):
        prv = self.right.prev 
        node.prev = prv
        prv.next = node
        node.next = self.right
        self.right.prev = node 

    def remove(self, node):
        prv, nxt = node.prev, node.next 
        prv.next = nxt
        nxt.prev = prv



    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        else:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.hm:
            newNode = Node(key, value)
            self.hm[key] = newNode
            self.insert(newNode)
            if self.capacity == self.currLen:
                lru = self.left.next
                self.remove(lru)
                self.currLen-=1
                del self.hm[lru.key]
            self.currLen+=1
        else:
            node = self.hm[key]
            node.val = value
            self.remove(self.hm[key])
            self.insert(node)
            self.hm[key] = node
        
        
