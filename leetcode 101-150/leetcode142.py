# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        fast, slow = head.next.next, head.next
        while fast and fast.next:
            if fast == slow:
                while slow != head:
                    head = head.next
                    slow = slow.next

                return slow

            fast = fast.next.next
            slow = slow.next

        return None

