class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_sequence = version1.split('.')
        version2_sequence = version2.split('.')

        version1_start, version2_start = 0, 0
        while version1_start < len(version1_sequence) or version2_start < len(version2_sequence):
            version1_value, version2_value = 0, 0
            if version1_start < len(version1_sequence):
                version1_value = int(version1_sequence[version1_start])

            if version2_start < len(version2_sequence):
                version2_value = int(version2_sequence[version2_start])

            if version1_value != version2_value:
                return version1_value > version2_value and 1 or -1
            
            version1_start += 1
            version2_start += 1

        return 0

x = Solution()
print(x.compareVersion('0.1', '1.1') == -1)
print(x.compareVersion('1.0.1', '1') == 1)
print(x.compareVersion('7.5.2.4', '7.5.3') == -1)
print(x.compareVersion('01', '1') == 0)
print(x.compareVersion('1.2', '1.10') == -1)
print(x.compareVersion('1.0', '1') == 0)
