class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        sol = []
        heapify(sol)

        for i in (arr):
            heappush(heap,(abs(x - i), i))
        
        while k:
            h = heappop(heap)
            heappush(sol, h[1])
            k-=1
        
        return sorted(sol)