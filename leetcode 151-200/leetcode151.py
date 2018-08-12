class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for word in s.split(' '):
            if word:
                res.append(word)

        return ' '.join(res[::-1])


x = Solution()
print(x.reverseWords('the sky is blue') == 'blue is sky the')
