# Definition for singly-linked list.
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
        return '<ListNode {}>'.format(self.val)
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next

        return '<ListNode {}>'.format(vals)

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def get_end(root):
            nodes = []
            while root:
                nodes.append(root) 
                root = root.next

            while nodes:
                node = nodes.pop()
                if nodes:
                    nodes[-1].next = None

                yield node

        end_generate = get_end(head)
        current = head
        while current and current.next:
            try:
                end_node = next(end_generate)
            except StopIteration:
                return head

            if current == end_node:
                return head

            current.next, end_node.next = end_node, current.next
            current = end_node.next

        return head

x = Solution()
ListNode.printof(x.reorderList(ListNode.generate_node([1, 2, 3, 4])))
print ('fds')
ListNode.printof(x.reorderList(ListNode.generate_node([1, 2, 3, 4, 5])))
