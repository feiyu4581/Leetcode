from collections import defaultdict
import heapq

class Solution:
    def getSkyline2(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        res = []
        currents = []
        steps = []
        for building in buildings:
            steps.extend([building[0], building[1]])
        
        steps.sort()

        buildings = list(reversed(buildings))
        for index in steps:
            in_buildings, out_buildings = [], []
            while buildings and buildings[-1][0] == index:
                in_buildings.append(buildings.pop())

            max_height = 0
            for current in currents:
                if current[1] == index:
                    out_buildings.append(current)
                else:
                    max_height = max(max_height, current[2])

            in_point, out_point = [index, 0], [index, 0]
            for building in in_buildings:
                in_point = [index, max(in_point[1], building[2])]
                currents.append(building)

            for building in out_buildings:
                out_point = [index, max(out_point[1], building[2])]
                currents.remove(building)

            if in_point[1] > 0 and in_point[1] != out_point[1] and in_point[1] > max_height:
                res.append(in_point)

            if out_point[1] > 0 and out_point[1] != in_point[1] and out_point[1] > max_height:
                res.append([index, max_height])

        return res

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        res, currents, steps = [], [], []
        for building in buildings:
            steps.extend([building[0], building[1]])

        steps = list(set(steps))
        steps.sort()

        in_maps, out_maps = defaultdict(list), defaultdict(list)
        for building in buildings:
            in_maps[building[0]].append(building)
            out_maps[building[1]].append(building)

        max_height, last_max_height = 0, 0
        for index in steps:
            in_buildings, out_buildings = in_maps[index], out_maps[index]

            in_point, out_point = [index, 0], [index, 0]
            for building in out_buildings:
                out_point = [index, max(out_point[1], building[2])]
                currents.remove(building)

            if out_buildings:
                if currents:
                    last_max_height = max(map(lambda current: current[2], currents))
                else:
                    last_max_height = 0

            max_height = last_max_height

            for building in in_buildings:
                in_point = [index, max(in_point[1], building[2])]
                currents.append(building)
                last_max_height = max(last_max_height, building[2])

            if in_point[1] > 0 and in_point[1] != out_point[1] and in_point[1] > max_height:
                res.append(in_point)

            if out_point[1] > 0 and out_point[1] != in_point[1] and out_point[1] > max_height:
                res.append([index, max_height])

        return res


x = Solution()
print(x.getSkyline([[0,2147483647,2147483647]]))
print(x.getSkyline([
    [2, 9, 10],
    [3, 7, 15],
    [5, 12, 12],
    [15, 20, 10],
    [19, 24, 8] 
]) == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ])

