class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = piles
        ans = 0

        while queue:
            queue.pop()
            ans += queue.pop()
            queue.pop(0)
        return ans