class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tracker = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            tracker.append(min(tracker[i-2]+cost[i], 
                              tracker[i-1]+cost[i]
                              ))

        return min(tracker[-1], tracker[-2])