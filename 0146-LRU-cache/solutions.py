class LRUCache(object):

    class Node:
        def __init__(self, val=None, prev=None, next=None):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.nodeMap = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not self.nodeMap.get(key):
            return -1

        value, node = self.nodeMap.get(key)
        self.move_to_tail(node)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nodeMap:
            self.nodeMap[key][0] = value
            self.move_to_tail(self.nodeMap[key][1])
            return

        if len(self.nodeMap) == self.capacity:
            del_key = self.head.val
            if self.head.next is None:
                self.tail = None
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
            del self.nodeMap[del_key]
        
        if not self.nodeMap:
            self.head = self.Node(key)
            self.tail = self.head
        else:
            self.tail.next = self.Node(key, self.tail, None)
            self.tail = self.tail.next
        
        self.nodeMap[key] = [value, self.tail]

    def move_to_tail(self, node):
        if node is self.tail:
            return

        if node is self.head:
            self.head = self.head.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = None