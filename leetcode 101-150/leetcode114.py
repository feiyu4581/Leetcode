# Definition for a binary tree node.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def generate_node(cls, vals):
        root, current = None, None
        for val in vals:
            node = cls(val)
            if not root:
                root = node

            if current:
                current.next = node

            current = node

        return root

    @staticmethod
    def printof(head):
        current = head
        while current:
            print (current.val)
            current = current.next

    def __repr__(self):
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next

        return '<ListNode {}>'.format(vals)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.val)


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if node:
                if not node.left and not node.right:
                    return node

                left_end = preorder(node.left)
                _ = preorder(node.right)

                right_node = node.right
                if node.left:
                    node.right = node.left
                    if left_end:
                        left_end.right = right_node

                node.left = None

                while right_node and right_node.right:
                    right_node = right_node.right

                return right_node or left_end

        preorder(root)
        return root


x = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(5)
root.left.right = TreeNode(4)

x.flatten(root)
