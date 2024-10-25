class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity 
        steps = 0

        for i in range(len(plants)):
            if curr < plants[i]:
                curr = capacity
                steps += 2*i
            steps += 1
            curr -= plants[i]


        return (steps)