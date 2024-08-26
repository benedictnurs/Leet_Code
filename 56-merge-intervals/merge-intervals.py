class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        sol = []
        l = 0

        for r in range(1, len(intervals)):
            if intervals[r][0] <= intervals[l][1]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
            else:
                sol.append(intervals[l])
                l = r
        
        sol.append(intervals[l])
        return sol