class MyHashSetBST(object):

    def __init__(self):
        self.capacity = 769
        self.set = [self.BST() for i in range(self.capacity)]
        self.size = 0

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.set[self.hash_function(key)]
        bucket.insert(key)
                
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.set[self.hash_function(key)]
        bucket.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        bucket = self.set[self.hash_function(key)]
        return bucket.contains(key)
    
    def hash_function(self, key):
        return key % self.capacity

    class BST:
        class Node:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

        def __init__(self):
            self.root = None

        def insert(self, val):
            
            def insert_helper(root, val):
                if root is None:
                    return self.Node(val)
                
                if root.val < val:
                    root.right = insert_helper(root.right, val)
                elif root.val > val:
                    root.left = insert_helper(root.left, val)
                
                return root
            
            self.root = insert_helper(self.root, val)

        def remove(self, val):
            
            def get_min(root):
                current = root
                while current and current.left:
                    current = current.left
                return current

            def remove_helper(root, val):
                if root is None:
                    return root
                
                if root.val < val:
                    root.right = remove_helper(root.right, val)
                elif root.val > val:
                    root.left = remove_helper(root.left, val)
                else:
                    if root.left is None:
                        return root.right
                    elif root.right is None:
                        return root.left
                    else:
                        right_min = get_min(root.right)
                        root.val = right_min.val
                        root.right = remove_helper(root.right, val)
                
                return root
            
            self.root = remove_helper(self.root, val)

        
        def contains(self, val):
            def bst(root, val):
                if root is None:
                    return False
                
                if root.val < val:
                    return bst(root.right, val)
                elif root.val > val:
                    return bst(root.left, val)
                else:
                    return True
            
            return bst(self.root, val)

class MyHashSetLinkedListApproach(object):
 
    def __init__(self):
        self.capacity = 2
        self.set = [self.LinkedList(), self.LinkedList()]
        self.size = 0

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash_function(key)

        if not self.set[hash_value].containskey(key):
            self.set[hash_value].addkey(key)
            self.size += 1

        if self.size >= self.capacity // 2:
            self.rehash()
                
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash_function(key)
        self.set[hash_value].removekey(key)
        self.size -= 1

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_value = self.hash_function(key)
        return self.set[hash_value].containskey(key)
    
    def hash_function(self, key):
        total = 0
        for c in str(key):
            total += ord(c)

        return total % self.capacity

    def rehash(self):
        self.capacity *= 2
        new_list = []
        for _ in range(self.capacity):
            new_list.append(self.LinkedList())

        self.size = 0
        old_list = self.set
        self.set = new_list

        for linked_list in old_list:
            current = linked_list.head
            while current: 
                if current.key: # Used dummy heads so need to account for that.
                    self.add(current.key)
                current = current.next
    
    class LinkedList:
        class Node:
            def __init__(self, key, next = None):
                self.key = key
                self.next = next

        def __init__(self):
            self.head = self.Node(None)
            self.tail = self.head

        def containskey(self, key):
            current = self.head.next
            while current:
                if current.key == key:
                    return True
                current = current.next

            return False 

        def addkey(self, key):
        
            self.tail.next = self.Node(key)
            self.tail = self.tail.next
        
        def removekey(self, key):
            current = self.head

            while current.next:
                if current.next.key == key:
                    if current.next is self.tail:
                        self.tail = current
                    current.next = current.next.next
                    break
                
                current = current.next


class MyHashSetQuadraticProbingDoublingResizeTooSlow(object):
    
    def __init__(self):
        self.capacity = 2
        self.set = [None, None]
        self.size = 0

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash_function(key)
        i = 1
        while True:
            if self.set[hash_value] == key:
                return

            if self.set[hash_value] is None:
                self.set[hash_value] = key
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return

            hash_value = (hash_value + i ** i) % self.capacity
            i += 1
                
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash_function(key)
        i = 1
        while True:
            if self.set[hash_value] is None:
                return
            
            if self.set[hash_value] == key:
                self.set[hash_value] = -1
                return
            
            hash_value = (hash_value + i ** i) % self.capacity
            i += 1

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_value = self.hash_function(key)
        i = 1
        while True:
            if self.set[hash_value] is None:
                return False
            
            if self.set[hash_value] == key:
                return True

            hash_value = (hash_value + i ** i) % self.capacity
            i += 1
    
    def hash_function(self, key):
        total = 0
        for c in str(key):
            total += ord(c)

        return total % self.capacity

    def rehash(self):
        self.capacity *= 2
        new_list = [None] * self.capacity
        self.size = 0
        old_list = self.set
        self.set = new_list

        for key in old_list:
            if key and key != -1:
                self.add(key)

class MyHashSetLinearProbingTooDoubleRehashingTooSlow(object):
    
    def __init__(self):
        self.capacity = 2
        self.set = [None, None]
        self.size = 0

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash_function(key)
        for _ in range(self.capacity):
            if self.set[hash_value] == key:
                return

            if self.set[hash_value] is None:
                self.set[hash_value] = key
                self.size += 1
                if self.size >= self.capacity:
                    self.rehash()
                return

            hash_value = (hash_value + 1) % self.capacity
                
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash_function(key)
        for _ in range(self.capacity):
            if self.set[hash_value] is None:
                return
            
            if self.set[hash_value] == key:
                self.set[hash_value] = -1
                return
            
            hash_value = (hash_value + 1) % self.capacity

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_value = self.hash_function(key)
        for _ in range(self.capacity):
            if self.set[hash_value] is None:
                return False
            
            if self.set[hash_value] == key:
                return True

            hash_value = (hash_value + 1) % self.capacity
    
    def hash_function(self, key):
        total = 0
        for c in str(key):
            total += ord(c)

        return total % self.capacity

    def rehash(self):
        self.capacity *= 2
        new_list = [None] * self.capacity
        self.size = 0
        old_list = self.set
        self.set = new_list

        for key in old_list:
            if key and key != -1:
                self.add(key)