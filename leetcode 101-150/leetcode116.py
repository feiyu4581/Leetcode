# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def _connect(root):
            if root and root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left

                _connect(root.left)
                _connect(root.right)

        _connect(root)
    
    def connect2(self, root):
        def _connect(left, right):
            if left and right:
                left.next = right

                _connect(left.left, left.right)
                _connect(right.left, right.right)
                _connect(left.right, right.left)

        if root:
            _connect(root.left, root.right)


x = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)

x.connect(root)
print(root.next)
print(root.left.next)
print(root.right.next)
        