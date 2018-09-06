# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        if root:
            stack.append([root])

        while stack:
            nodes = stack.pop()
            res.append(nodes[0].val)
            next_nodes = []
            for node in nodes:
                if node.right:
                    next_nodes.append(node.right)

                if node.left:
                    next_nodes.append(node.left)

            if next_nodes:
                stack.append(next_nodes)

        return res

x = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print (x.rightSideView(root) == [1, 3, 4])