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
        vals = []
        while current:
            vals.append(current.val)
            current = current.next

        print (','.join(map(str, vals)))

    def __repr__(self):
        return '<ListNode {}>'.format(self.val)

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy
        while left and right:
            if left.val > right.val:
                current.next = right
                right = right.next
            else:
                current.next = left
                left = left.next

            current = current.next

        current.next = left or right
        return dummy.next


x = Solution()
ListNode.printof(x.sortList(ListNode.generate_node([4, 2, 1, 3])))
ListNode.printof(x.sortList(ListNode.generate_node([-1, 5, 3, 4, 0])))
