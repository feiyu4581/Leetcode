# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        left_height = self.get_left_height(root)
        right_height = self.get_right_height(root)

        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def get_left_height(self, root):
        height = 0
        current = root
        while current:
            height += 1
            current = current.left

        return height

    def get_right_height(self, root):
        height = 0
        current = root
        while current:
            height += 1
            current = current.right

        return height

    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queues = [(root, 0)]
        min_depth, diff_offset = None, 0
        while queues:
            node, depth = queues.pop()
            if node.left:
                queues.append((node.left, depth + 1))

            if node.right:
                queues.append((node.right, depth + 1))

            if not node.right or not node.left:
                if min_depth is None:
                    min_depth = depth
                elif depth > min_depth:
                    return 2 ** (min_depth + 2) - 1 - diff_offset

            if not node.left:
                diff_offset += 1

            if not node.right:
                diff_offset += 1

        return 2 ** (min_depth + 1) - 1


x = Solution()

root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

print(x.countNodes(root))
