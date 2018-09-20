class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        location = 0
        for index in range(0, len(s) // 2 + 1):
            left, right = s[index::-1], s[index:index + index + 1]
            if left == right:
                location = max(index + index, location)

            left, right = s[index::-1], s[index + 1:index + index + 2]
            if left == right:
                location = max(index + index + 1, location)

        return s[:location:-1] + s

    def shortestPalindrome2(self, s):
        # TODO: 将翻转子串合并到s中，然后使用kmp算法求解前缀和后缀
        pass


x = Solution()
print(x.shortestPalindrome('aacecaaa') == 'aaacecaaa')
print(x.shortestPalindrome('abcd') == 'dcbabcd')
print(x.shortestPalindrome('aba') == 'aba')
print(x.shortestPalindrome('aabba') == 'abbaabba')
