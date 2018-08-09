# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return res

    def preorderTraversal(self, root):
        if not root:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return res


x = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(x.preorderTraversal(root) == [1, 2, 3])
        