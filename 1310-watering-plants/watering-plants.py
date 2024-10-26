class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity 
        steps = 0

        for i in range(len(plants)):
            if plants[i] > curr:
                steps += i*2
                curr = capacity
            curr -= plants[i]
            steps += 1

        return steps