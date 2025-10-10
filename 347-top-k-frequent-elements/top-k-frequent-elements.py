class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        sol = []

        for key,value in count.items():
            heappush(heap,(-value,key))
        

        while k:
            sol.append(heappop(heap)[1])
            k -= 1
        
        return sol
