class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        key_maps, right_key_maps = {}, {}
        for left, right in zip(s, t):
            if left in key_maps and key_maps[left] != right:
                return False

            if right in right_key_maps and right_key_maps[right] != left:
                return False

            key_maps[left] = right
            right_key_maps[right] = left

        return True


x = Solution()
print(x.isIsomorphic('egg', 'add') == True)
print(x.isIsomorphic('foo', 'bar') == False)
print(x.isIsomorphic('paper', 'title') == True)
print(x.isIsomorphic('ab', 'aa') == False)
        