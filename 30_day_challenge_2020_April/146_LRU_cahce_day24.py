################################################################
# Author            : yiorgosynkl (find me in Github: https://github.com/yiorgosynkl)
# Date created      : 20200424
# Problem link      : https://leetcode.com/problems/lru-cache/
################################################################

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.order = []
        self.cap = capacity 

    def get(self, key: int) -> int:
        if key in self.dic.keys():
            self.order.remove(key)
            self.order.insert(0, key)
            return self.dic[key]
        else:
            return -1
        
        
    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.dic[key] = value
        else:
            if len(self.order) == self.cap:
                exit_key = self.order.pop()
                del self.dic[exit_key]
            self.order.insert(0, key)
            self.dic[key] = value
            
# consice version
#     def __init__(self, capacity):
#         self.dic = collections.OrderedDict()
#         self.remain = capacity

#     def get(self, key):
#         if key not in self.dic:
#             return -1
#         v = self.dic.pop(key) 
#         self.dic[key] = v   # set key as the newest one
#         return v

#     def set(self, key, value):
#         if key in self.dic:    
#             self.dic.pop(key)
#         else:
#             if self.remain > 0:
#                 self.remain -= 1  
#             else:  # self.dic is full
#                 self.dic.popitem(last=False) 
#         self.dic[key] = value

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)