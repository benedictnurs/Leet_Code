class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        sol = [intervals[0]]

        for i in range(1, len(intervals)):
            if (sol[-1][1] >= intervals[i][0]):
                sol[-1][1] = max(intervals[i][1], sol[-1][1])
            else:
                sol.append(intervals[i])

        return(sol)
