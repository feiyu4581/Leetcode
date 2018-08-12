class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0

        stack = []
        operators = {
            '+': lambda one, two: one + two,
            '-': lambda one, two: one - two,
            '*': lambda one, two: one * two,
            '/': lambda one, two: one * two > 0 and one // two or -(abs(one) // abs(two))
        }
        for token in tokens:
            if token in operators:
                two, one = stack.pop(), stack.pop()
                stack.append(operators[token](one, two))
            else:
                stack.append(int(token))

        return stack.pop()


x = Solution()
print(x.evalRPN(["2", "1", "+", "3", "*"]) == 9)
print(x.evalRPN(["4", "13", "5", "/", "+"]) == 6)
print(x.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22)
        