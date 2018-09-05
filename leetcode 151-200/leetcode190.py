class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].rjust(32, '0')[::-1], 2)


x = Solution()
print(x.reverseBits(43261596) == 964176192