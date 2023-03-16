class MyHashMapBST(object):

    def __init__(self):
        self.capacity = 769
        self.map = [self.BST() for i in range(self.capacity)]
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket = self.map[self.hash(key)]
        bucket.add(key, value)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        bucket = self.map[self.hash(key)]
        node = bucket.get(key)
        
        if node:
            return node.val
        
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.map[self.hash(key)]
        bucket.remove(key)

    def hash(self, key):
        return key % self.capacity

    class BST:

        class Node:
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.left = None
                self.right = None
            
        def __init__(self):
            self.root = None

        def add(self, key, val):

            def add_helper(root, key, val):
                if root is None:
                    return self.Node(key, val)
                
                if key < root.key:
                    root.left = add_helper(root.left, key, val)
                elif key > root.key:
                    root.right = add_helper(root.right, key, val)
                else:
                    root.val = val
                
                return root
            
            self.root = add_helper(self.root, key, val)

        def get(self, key):

            def get_helper(root, key):
                if root is None:
                    return root

                if key < root.key:
                    return get_helper(root.left, key)
                elif key > root.key:
                    return get_helper(root.right, key)
                else:
                    return root
            
            return get_helper(self.root, key)

        def remove(self, key):
            
            def get_min(root):
                current = root
                while current and current.left:
                    current = current.left
                return current

            def remove_helper(root, key):
                if root is None:
                    return root

                if key < root.key:
                    root.left = remove_helper(root.left, key)
                elif key > root.key:
                    root.right = remove_helper(root.right, key)
                else:
                    if root.left is None:
                        return root.right
                    elif root.right is None:
                        return root.left
                    else:
                        right_min = get_min(root.right)
                        root.key = right_min.key
                        root.val = right_min.val
                        root.right = remove_helper(root.right, right_min.key)

                return root
            
            self.root = remove_helper(self.root, key)

class MyHashMapOpenAddressing(object):

    class Pair:
        def __init__(self, key, val):
            self.key = key
            self.val = val

    def __init__(self):
        self.capacity = 2
        self.map = [None, None]
        self.size = 0
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_value = self.hash(key)
        i = 1
        while True:
            if self.map[hash_value] is None:
                self.map[hash_value] = self.Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return

            if self.map[hash_value].key == key:
                self.map[hash_value].val = value
                return

            hash_value = (hash_value + i ** i) % self.capacity
            i += 1
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_value = self.hash(key)
        i = 1
        while True:
            if self.map[hash_value] is None:
                return -1
            
            if self.map[hash_value].key == key:
                return self.map[hash_value].val

            hash_value = (hash_value + i ** i) % self.capacity
            i += 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_value = self.hash(key)
        i = 1
        while True:
            if self.map[hash_value] is None:
                return
            
            if self.map[hash_value].key == key:
                self.map[hash_value].val = -1
                return
            
            hash_value = (hash_value + i ** i) % self.capacity
            i += 1
    
    def hash(self, key):
        return key % self.capacity

    def rehash(self):
        self.capacity *= 2
        new_list = [None] * self.capacity
        self.size = 0
        old_list = self.map
        self.map = new_list

        for pair in old_list:
            if pair and pair.key != -1:
                self.put(pair.key, pair.val)