class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = low
        while low <= high:
            mid = (low + high) // 2
            time = 0
            for i in piles:
                time += math.ceil(float(i)/mid)
            if time <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res