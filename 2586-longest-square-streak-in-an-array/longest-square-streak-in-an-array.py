from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = {}
        visited = set()  # Keep track of numbers we've already processed
        nums.sort()
        streak = -1  # Initialize streak to -1, as requested

        # Create a mapping of each number to its square
        for i in nums:
            seen[i] = i * i

        # Loop through each number to calculate streaks
        for i in nums:
            if i in visited:
                continue  # Skip if we've already processed this number

            count = 0  # Start with the number itself
            current = i

            while current in seen and seen[current] not in visited:
                visited.add(current)  # Mark as processed
                current = seen[current]  # Move to its square
                count += 1  # Increment streak length

            # Update streak if this is the longest we've seen
            streak = max(streak, count)

        return streak if streak > 1 else -1  # Return -1 if no valid streak found
