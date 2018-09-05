class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sets, res = set(), set()
        for index in range(0, len(s) - 10 + 1):
            current = s[index:index + 10]
            if len(current) != 10:
                break

            if current not in sets:
                sets.add(current)
            else:
                res.add(current)

        return list(res)

x = Solution()
print(x.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT') == ["AAAAACCCCC", "CCCCCAAAAA"])
print(x.findRepeatedDnaSequences('AAAAAAAAAAA') == ["AAAAAAAAAA"])
print(x.findRepeatedDnaSequences('AAAAAAAAAAAA') == ['AAAAAAAAAA'])
        