# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return

        nodes, seen, queue = {}, set(), [node]
        nodes[node] = UndirectedGraphNode(node.label)
        while queue:
            vector = queue.pop()
            if vector not in seen:
                seen.add(vector)

                for neighbor in vector.neighbors:
                    if neighbor not in nodes:
                        nodes[neighbor] = UndirectedGraphNode(neighbor.label)
                        
                    nodes[vector].neighbors.append(nodes[neighbor])
                    queue.append(neighbor)

        return nodes[node]


x = Solution()
node_0 = UndirectedGraphNode(0)
node_1 = UndirectedGraphNode(1)
node_2 = UndirectedGraphNode(2)

node_0.neighbors = [node_1, node_2]
node_1.neighbors = [node_0, node_2]
node_2.neighbors = [node_0, node_1, node_2]
print(x.cloneGraph(node_0))
        