class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        sol = []
        l = 0
     
        for r in range(1, len(intervals)):
            #If the ending of the left greater than start of the right
            #Ending of the left will be the maximum out of the endings
            if intervals[r][0] <= intervals[l][1]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
            else:
            #Else just append and move the left to the current index
                sol.append(intervals[l])
                l = r
        
        sol.append(intervals[l])
        return sol