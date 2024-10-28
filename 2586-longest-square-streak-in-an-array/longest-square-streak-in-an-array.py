class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = {}
        visited = set() 
        nums.sort()
        streak = -1
        
        for i in nums:
            seen[i] = i * i

        for i in nums:
            if i in visited:
                continue
                    
            count = 0
            current = i
            
            while current in seen and seen[current] not in visited:
                visited.add(current)
                current = seen[current]
                count += 1

            streak = max(count,streak)

        return streak if streak > 1 else -1