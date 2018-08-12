# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'<ListNode: {self.val}>'


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        start_a, start_b = headA, headB
        while True:
            if start_a is start_b:
                return start_a

            start_a = start_a.next
            start_b = start_b.next

            if not start_a and not start_b:
                return None

            if not start_a:
                start_a = headB

            if not start_b:
                start_b = headA


x = Solution()

node_a1 = ListNode('a1')
node_a2 = ListNode('a2')

node_b1 = ListNode('b1')
node_b2 = ListNode('b2')
node_b3 = ListNode('b3')

node_c1 = ListNode('c1')
node_c2 = ListNode('c2')


node_a1.next = node_a2
node_a2.next = node_c1
node_c1.next = node_c2

node_b1.next = node_b2
node_b2.next = node_b3
node_b3.next = node_c1

print(x.getIntersectionNode(node_a1, node_b1) == node_c1)
