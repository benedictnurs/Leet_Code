class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        sol = 0

        while l < r:
            volume = min(height[l], height[r]) * (r - l)
            sol = max(volume, sol)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1    
        

        return sol