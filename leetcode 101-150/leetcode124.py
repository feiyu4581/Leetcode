# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        areas = []
        def path_sum(node):
            if node:
                left_value = path_sum(node.left)
                right_value = path_sum(node.right)

                areas.append(max(left_value, 0) + node.val + max(right_value, 0))
                areas.append(max(max(left_value, 0) + node.val, max(right_value, 0) + node.val))
                return areas[-1]

            return 0

        path_sum(root)
        return max(areas)

    def maxPathSum(self, root):
        def path_sum(node):
            if node:
                left_max, left_path = path_sum(node.left)
                right_max, right_path = path_sum(node.right)

                node_max = max(left_max, right_max, left_path + node.val + right_path)
                node_path = max(left_path + node.val, right_path + node.val, 0)

                return node_max, node_path
            return float('-inf'), 0

        res, _ = path_sum(root)
        return res

x = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(x.maxPathSum(root) == 6)
        
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(x.maxPathSum(root) == 42)

root = TreeNode(2)
root.left = TreeNode(-1)
print(x.maxPathSum(root) == 2)