import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        heap = []
        for number, count in nums.items():
            heapq.heappush(heap,(-count,number))


        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res