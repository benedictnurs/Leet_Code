class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        sol = 0

        for i in nums:
            heappush(heap, -i)
        
        while k:
            k -= 1
            sol = heappop(heap)

        return -sol