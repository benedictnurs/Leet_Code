class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        sol = []

        for point in points:
            distance = sqrt((0 - point[0])** 2+(0 - point[1])**2)
            heappush(heap,(distance, point))

        while k:
            sol.append(heappop(heap)[1])
            k -= 1
        
        return sol