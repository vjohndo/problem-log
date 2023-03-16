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
