class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)

        sol = [intervals[0]]

        for i in range(1, len(intervals)):
            if sol[-1][1] >= intervals[i][0]:
                sol[-1][1] = max(sol[-1][1], intervals[i][1])
            else:
                sol.append(intervals[i])

        return sol