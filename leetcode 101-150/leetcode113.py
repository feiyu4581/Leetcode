# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res, temp = [], []
        def path(head, pre_sum):
            if not head:
                return False

            if not head.left and not head.right and head.val + pre_sum == sum:
                res.append(temp[:])

            if head.left:
                temp.append(head.left.val)
                path(head.left, pre_sum + head.val)
                temp.pop()
            if head.right:
                temp.append(head.right.val)
                path(head.right, pre_sum + head.val)
                temp.pop()

        temp.append(root.val)
        path(root, 0)

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
x = Solution()
print(x.pathSum(root, 30))
        