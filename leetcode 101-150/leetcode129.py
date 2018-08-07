# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def sum_numbers(node, num):
            nonlocal res
            if node:
                current_val = num * 10 + node.val
                if not node.left and not node.right:
                    res += current_val

                sum_numbers(node.left, current_val)
                sum_numbers(node.right, current_val)

        sum_numbers(root, 0)
        return res


x = Solution()
root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)
print(x.sumNumbers(root) == 1026)
        