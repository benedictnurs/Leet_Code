class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        sol = []



        for key,value in count.items():
            heappush(heap, (-value, key))
        
        while k:
            print(k)
            k -= 1
            sol.append(heappop(heap)[1])

        return (sol)