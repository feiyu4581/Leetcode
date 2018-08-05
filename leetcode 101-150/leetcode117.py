# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def find_next(node):
            if node:
                current = node
                while current.next:
                    current = current.next
                    if current.left or current.right:
                        return current.left or current.right

            return None

        def _connect(node):
            if node:
                if node.left and node.right:
                    node.left.next = node.right

                if node.left or node.right:
                    right_node = node.right or node.left
                    right_node.next = find_next(node)

                # 必须先执行右边的内容后才能执行左边，因为左边的数据依赖于右边的 node.next 值
                _connect(node.right)
                _connect(node.left)

        _connect(root)



x = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.left.left = TreeLinkNode(4)
root.right = TreeLinkNode(3)
root.right.right = TreeLinkNode(4)

x.connect(root)
print(root.left.left.next)
        