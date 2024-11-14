class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in set(nums):
            heapq.heappush(heap, (-(nums.count(i)), i))
        print(heap)

        sol = []

        while k:
            sol.append(heapq.heappop(heap)[1])
            k-=1
        return (sol)