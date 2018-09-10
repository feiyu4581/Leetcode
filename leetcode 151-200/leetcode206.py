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
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next

        return '<ListNode {}>'.format(vals)


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        prev, current = head, head.next
        prev.next = None
        while current:
            next_node = current.next
            current.next = prev

            prev, current = current, next_node

        return prev


x = Solution()
ListNode.printof(x.reverseList(ListNode.generate_node([1, 2, 3, 4, 5])))
        