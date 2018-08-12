class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_value = float('inf')
        self.stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.min_value:
            self.min_value = x

        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        value = self.stack.pop()
        if self.stack:
            self.min_value = min(self.stack)
        else:
            self.min_value = float('inf')

        return value
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value


stack = MinStack()
stack.push(-2)