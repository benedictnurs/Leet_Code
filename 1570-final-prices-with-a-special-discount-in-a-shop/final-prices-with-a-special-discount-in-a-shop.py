"""
Stack
Use a copy becase we want to keep the orginal elements
Use an index based stack because it wants us to hold a minimum index

"""

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        initial = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                initial[stack.pop()] -= prices[i]
            stack.append(i)

        return initial