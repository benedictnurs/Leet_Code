class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        if duration == 0:
            return 0
        
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] <= duration:
                total += timeSeries[i+1] - timeSeries[i]
                print(total)
            else:
                total += duration
        
        total+= duration
        
        return total