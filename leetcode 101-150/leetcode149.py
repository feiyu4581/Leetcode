# Definition for a point.
from collections import Counter
from decimal import Decimal

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_area = 0
        for start in range(len(points)):
            repeat_nums = 1
            lines = Counter()
            for end in range(len(points)):
                if start == end:
                    continue
                elif points[start].x == points[end].x and points[start].y == points[end].y:
                    repeat_nums += 1
                else:
                    if points[start].x == points[end].x:
                        lines.update({float('inf'): 1})
                    else:
                        k = Decimal(str(points[start].y - points[end].y)) / Decimal(str(points[start].x - points[end].x))
                        lines.update({k: 1})

            if lines:
                max_area = max(lines.most_common(1)[0][1] + repeat_nums, max_area)
            else:
                max_area = max(max_area, repeat_nums)

        return max_area

x = Solution()
# print(x.maxPoints([
#     Point(1, 1),
#     Point(2, 2),
#     Point(3, 3)
# ]) == 3)

# print(x.maxPoints([
#     Point(1, 1),
#     Point(3, 2),
#     Point(5, 3),
#     Point(4, 1),
#     Point(2, 3),
#     Point(1, 4),
# ]) == 4)

print(x.maxPoints([
    Point(0, 0),
    Point(94911151, 94911150),
    Point(94911152, 94911151)
]) == 2)
