from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        paths = defaultdict(list)
        for requisties in prerequisites:
            paths[requisties[1]].append(requisties[0])

        all_exists = {}
        def dfs(course, exists, sequence):
            exists.add(course)

            sequence += 1
            next_sequence = sequence
            for next_course in paths[course]:
                if next_course in exists:
                    return False

                temp_sequence = dfs(next_course, exists, sequence)
                if not temp_sequence:
                    return False

                next_sequence = max(next_sequence, temp_sequence)

            exists.remove(course)
            sequence = next_sequence + 1
            all_exists[course] = sequence

            return sequence

        sequence = 0
        for course in range(numCourses):
            if course not in all_exists:
                sequence = dfs(course, set(), sequence)
                if not sequence:
                    return []

        res = [(course, sequence) for course, sequence in all_exists.items()]
        res = [
            course[0]
            for course in sorted(res, key=lambda course: course[1], reverse=True)
        ]

        print('-----', all_exists, res)


x = Solution()
print(x.findOrder(3, [[2,0],[2,1]]) == [1,0,2])
# print(x.findOrder(2, [[1,0]]) == [0, 1])
# print(x.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in ([0,1,2,3], [0,2,1,3]))
# print(x.findOrder(1, []) == [0])

        