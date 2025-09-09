class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0

        for r in range(1,len(prices)):
            diff = prices[r] - prices[l]
            while prices[r] < prices[l]:
                l += 1
            profit = max(diff, profit)
            print(diff)
        return profit