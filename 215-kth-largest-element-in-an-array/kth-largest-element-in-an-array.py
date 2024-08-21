import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        ans = 0
        while k:
            ans = heapq.heappop(nums)
            k -= 1

        return -ans
        