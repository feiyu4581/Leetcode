# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        nodes = {}
        nodes[head] = RandomListNode(head.label)
        stack = [head]
        while stack:
            node = stack.pop()
            if node.next:
                if node.next not in nodes:
                    nodes[node.next] = RandomListNode(node.next.label)
                
                nodes[node].next = nodes[node.next]
                stack.append(node.next)

            if node.random:
                if node.random not in nodes:
                    nodes[node.random] = RandomListNode(node.random.label)

                nodes[node].random = nodes[node.random]

        return nodes[head]


x = Solution()
root = RandomListNode(0)
root.next = RandomListNode(1)
root.next.next = RandomListNode(2)
root.next.next.next = RandomListNode(3)
root.next.next.next.next = RandomListNode(4)
root.next.random = root.next.next.next.next

res = x.copyRandomList(root)

print('--', res.next.random.label)
