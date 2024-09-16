class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        print(timePoints)
        mins = []
        minTime = float("inf")
        for time in timePoints:
            hour, minute = map(int, time.split(":"))
            mins.append(hour * 60 + minute)

        for i in range(1, len(mins)):
            minTime = min(minTime, mins[i] - mins[i - 1])
        
        minTime = min(minTime, 1440 - (mins[-1] - mins[0]))
        return minTime