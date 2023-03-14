class LRUCacheDummyNodes(object):

    class Node:
        def __init__(self, key, val, prev = None, next = None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def addNode(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.addNode(self.cache[key])
            return self.cache[key].val

        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            current_node = self.removeNode(self.cache[key])
            current_node.val = value
            self.addNode(current_node)
            return
        
        if len(self.cache) == self.cap:
            deleted_node = self.removeNode(self.head.next)
            del self.cache[deleted_node.key]
        
        new_node = self.Node(key, value)
        self.addNode(new_node)
        self.cache[key] = new_node


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