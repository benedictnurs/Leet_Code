class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0 
        l = 0 

        for r in range(1, len(intervals)):
            if intervals[l][1] > intervals[r][0]:
                count += 1
            else:
                l = r

        return count
