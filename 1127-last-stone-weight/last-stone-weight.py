class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heappush(heap, -i)
        
        while len(heap) > 1:
            rock1 = heappop(heap)
            rock2 = heappop(heap)
            heappush(heap, -((-rock1)-(-rock2)))

        if heap:
            return -heap[0]
        else:
            return 0