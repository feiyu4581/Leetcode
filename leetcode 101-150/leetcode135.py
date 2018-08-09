class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candy = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
        return sum(candy)

    def candy2(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        directions = []
        start, before, before_direction = 0, ratings[0], 0
        for index, rating in enumerate(ratings):
            if rating == before:
                if before_direction == 0:
                    before = rating
                else:
                    directions.append((start, index - 1, before_direction))
                    start, before, before_direction = index - 1, rating, 0
            elif rating > before:
                if before_direction == 1:
                    before = rating
                else:
                    directions.append((start, index - 1, before_direction))
                    start, before, before_direction = index - 1, rating, 1
            else:
                if before_direction == -1:
                    before = rating
                else:
                    directions.append((start, index - 1, before_direction))
                    start, before, before_direction = index - 1, rating, -1

        directions.append((start, index, before_direction))

        before_direction = None
        res, before_max = 0, 0
        for index, direction in enumerate(directions):
            if direction[2] == 0:
                res += direction[1] - direction[0]
                if index == 0:
                    res += 1
                before_max = 1
            elif direction[2] == 1:
                res += sum(range(2, direction[1] - direction[0] + 2))
                before_max = direction[1] - direction[0] + 1
            else:
                res += sum(range(1, direction[1] - direction[0] + 1))
                current_max = max(before_max, direction[1] - direction[0] + 1)
                res += current_max - before_max
        
        return res


x = Solution()
print(x.candy([1,0,2]) == 5)
print(x.candy([1,3,4,5,2]) == 11)
print(x.candy([1,2,2]) == 4)
