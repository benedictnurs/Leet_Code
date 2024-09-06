class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        sol = []
        l = 0
        for r in range(1, len(intervals)):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
            else:
                sol.append(intervals[l])
                l = r
        sol.append(intervals[l])
        return (sol)
        

