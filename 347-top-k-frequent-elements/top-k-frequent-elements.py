class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        sol = []
        for key,val in Counter(nums).items():
            heappush(heap, (-(val),key))  

        while k:
            k-=1
            sol.append(heappop(heap)[1])
        return (sol)
        