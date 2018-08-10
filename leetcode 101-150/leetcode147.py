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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        before, current = dummy, head
        while current:
            start, next_current = dummy, current.next
            while start.next != current:
                if start.next.val > current.val:
                    start.next, current.next, before.next = current, start.next, next_current
                    current = next_current
                    break

                start = start.next
            else:
                before, current = current, next_current

        return dummy.next

x = Solution()
ListNode.printof(x.insertionSortList(ListNode.generate_node([4, 2, 1, 3])))
ListNode.printof(x.insertionSortList(ListNode.generate_node([-1, 5, 3, 4, 0])))
        