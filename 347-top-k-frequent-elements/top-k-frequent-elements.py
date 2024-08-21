import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        heap = []
        for number, count in nums.items():
            heapq.heappush(heap,(-count,number))

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k-=1

        return res