class SolutionRefactored(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def clone(node, cloned):
            if node is None:
                return None

            cloned[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in cloned:
                    clone(nei, cloned)
                
                cloned[node].neighbors.append(cloned[nei])
            
            return cloned[node]
        
        return clone(node, {})
                    

class SolutionBlindNC(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        clone_map = {}
        
        if node is None: # Could potentially throw this outside
            return 

        def clone(node):
            clone_map[node] = Node(node.val)
            
            for nei in node.neighbors:
                if nei not in clone_map:
                    clone(nei)
                    
                clone_map[node].neighbors.append(clone_map[nei])

            return clone_map[node]
                
        return clone(node)


class SolutionBlindRevision(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return node

        cloned = {}
        visit = set()

        def dfs(node):
            if node is None:
                return

            if node in visit:
                return
            
            if node.val not in cloned:
                cloned[node.val] = Node(node.val)
            
            for neighbor in node.neighbors:
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val)

                cloned[node.val].neighbors.append(cloned[neighbor.val])

            visit.add(node)

            for neighbor in node.neighbors:
                dfs(neighbor)

        dfs(node)

        return cloned[node.val]

class SolutionNC(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node] # NC will return neighbour 

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy
        
        return clone(node) if node else None
    

class SolutionOG(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return node

        original = node
        cloned = Node(node.val)

        visit_map = {}
        visit_map[node.val] = cloned

        visit_set = set()

        def clone(original, cloned):
            for neighbor in original.neighbors:
                if neighbor.val in visit_map:
                    cloned.neighbors.append(visit_map[neighbor.val])
                else:
                    new_node = Node(neighbor.val)
                    cloned.neighbors.append(new_node)
                    visit_map[neighbor.val] = new_node
                
            visit_set.add(cloned.val)

            for i in range(len(cloned.neighbors)):
                if cloned.neighbors[i].val in visit_set:
                    continue

                clone(original.neighbors[i], cloned.neighbors[i])

        clone(original, cloned)

        return cloned
