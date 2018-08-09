# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.append(node.val)
                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)
            else:
                res.append(node)
        
        return res

x = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(x.postorderTraversal(root) == [3, 2, 1])
        