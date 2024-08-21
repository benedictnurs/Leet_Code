import heapq
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        heapq.heapify(nums)

        while nums:
            minimum = heapq.heappop(nums)
            if minimum == 0:
                continue

            count += 1            
            nums = [i - minimum for i in nums]            
        
        return count