class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sol = []
        left = 0
        right = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                sol.append(nums[left]**2)
                left += 1
            else:
                sol.append(nums[right]**2)
                right -= 1
        
        return (sol[::-1])