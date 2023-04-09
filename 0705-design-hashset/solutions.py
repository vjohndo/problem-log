class MyHashSetBST(object):
    class BST:
        class Node:
            def __init__(self, key = None, val = None, left = None, right = None):
                self.key = key
                self.val = val
                self.left = left
                self.right = right
        
        def __init__(self):
            self.root = None
        
        def contains(self, key):

            def search_helper(root, key):
                if root is None:
                    return False
                
                if root.key < key:
                    return search_helper(root.right, key)
                elif root.key > key:
                    return search_helper(root.left, key)
                else:
                    return True
            
            return search_helper(self.root, key)
        
        def insert(self, key, val):
            def insert_helper(root, key, val):
                if root is None:
                    return self.Node(key, val)
                
                if root.key < key:
                    root.right = insert_helper(root.right, key, val)
                elif root.key > key:
                    root.left = insert_helper(root.left, key, val)
                # For a set, BST does not to deal with an else statement here;
                # if we find it's already in the set we do nothing... headache LOL

                return root # MAKE SURE TO RETURN ROOT. DO NOT USE ELSE
        
            self.root = insert_helper(self.root, key, val)
        
        def remove(self, key):
            def remove_helper(root, key):
                if root is None:
                    return root
                
                if root.key < key:
                    root.right = remove_helper(root.right, key)
                elif root.key > key:
                    root.left = remove_helper(root.left, key)
                else:
                    if root.left is None:
                        return root.right
                    elif root.right is None:
                        return root.left
                    else:
                        min_node = root.right
                        while min_node is not None and min_node.left is not None:
                            min_node = min_node.left
                        
                        root.key = min_node.key
                        root.val = min_node.val
                        root.right = remove_helper(root.right, min_node.key)
                
                return root # MAKE SURE TO RETURN
            
            self.root = remove_helper(self.root, key)

    def __init__(self):
        self.capacity = 769
        self.arr = [self.BST() for _ in range(self.capacity)]


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.arr[index]
        bucket.insert(key, None)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        bucket = self.arr[index]
        bucket.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self._hash(key)
        bucket = self.arr[index]
        return bucket.contains(key)

    
    def _hash(self, key):
        return key % self.capacity

class MyHashSetLinkedListApproachAndRehashing(object):
 
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

class MyHashSetQuadraticProbingRehashingRefactored(object):
    def __init__(self):
        self.capacity = 2
        self.arr = [None, None]
        self.size = 0

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)

        i = 1
        while self.arr[index] != key:
            if self.arr[index] is None:
                self.arr[index] = key
                self.size += 1
                if self.size >= self.capacity // 2:
                    self._rehash()
                return
            
            index = (index + (i ** i)) % self.capacity
            i += 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        
        i = 1
        while self.arr[index] is not None:
            if self.arr[index] == key:
                self.arr[index] = -1
                return
            
            index = (index + (i ** i)) % self.capacity
            i += 1
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self._hash(key)

        i = 1
        while self.arr[index] is not None:
            if self.arr[index] == key:
                return True
            
            index = (index + (i ** i)) % self.capacity
            i += 1
        
        return False

    def _hash(self, key):
        return key % self.capacity
    
    def _rehash(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        
        old_arr = self.arr
        self.arr = new_arr
        self.size = 0

        for key in old_arr:
            if key and key != -1:
                self.add(key)

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
    
    def hash_function(self, key): # Don't use this in submissions
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