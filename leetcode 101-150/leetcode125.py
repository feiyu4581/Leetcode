class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        low, high = 0, len(s) - 1
        while low < high:
            if not s[low].isalnum():
                low += 1
            elif not s[high].isalnum():
                high -= 1
            elif s[low] != s[high]:
                return False
            else:
                low += 1
                high -= 1

        return True
            

x = Solution()
print(x.isPalindrome('A man, a plan, a canal: Panama') == True)
print(x.isPalindrome('race a car') == False)
        