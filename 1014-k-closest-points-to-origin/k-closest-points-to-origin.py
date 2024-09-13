class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        sol = []
        for point in points:
            distance = (sqrt((0 - point[0])**2 + (0 - point[1])**2), point)
            heappush(heap,distance)
        
        print(heap)

        while k:
            coords = heappop(heap)
            sol.append(coords[1])
            k-=1
        
        print(sol)

        return sol