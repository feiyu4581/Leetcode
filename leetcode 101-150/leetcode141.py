# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        fast, slow = head.next.next, head.next
        while fast != slow:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True
        

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head:
            if head in seen:
                return True
            
            seen.add(head)
            head = head.next

        return False

        