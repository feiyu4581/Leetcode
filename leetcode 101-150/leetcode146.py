class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return '<ListNode {}: {}>'.format(self.key, self.val)


class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.length = capacity
        self.current_length = 0
        self.store = {}
        self.start = None
        self.end = None

    
    def up(self, node):
        if not node is self.end:
            if node.prev:
                node.prev.next, node.next.prev = node.next, node.prev
            else:
                self.start, node.next.prev = node.next, None

            if self.end.prev is node:
                self.end.prev = None

            self.end.next, node.prev, node.next = node, self.end, None
            self.end = node

    def pop_start(self):
        old_start = self.start

        self.start = self.start.next
        self.start.prev, old_start.prev, old_start.next = None, None, None
        del self.store[old_start.key]


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.store:
            self.up(self.store[key])
            return self.store[key].val
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.store:
            node = ListNode(key, value)
            self.store[key] = node

            if not self.start:
                self.start = self.end = node
                self.current_length = 1
            else:
                self.end.next, node.prev = node, self.end
                self.end = node

                if self.current_length == self.length:
                    self.pop_start()
                else:
                    self.current_length += 1
        else:
            self.store[key].val = value
            self.up(self.store[key])


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.put(2, 1)
cache.put(2, 2)
print(cache.get(1) == 1)
cache.put(3, 3)   
print(cache.get(2) == -1)
cache.put(4, 4)
print(cache.get(1) == -1)
print(cache.get(3) == 3)
print(cache.get(4) == 4)
