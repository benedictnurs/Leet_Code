class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        sol = []
        for i in set(nums):
            heappush(heap, (-(nums.count(i)),i))  

        while k:
            k-=1
            sol.append(heappop(heap)[1])
        return (sol)
        