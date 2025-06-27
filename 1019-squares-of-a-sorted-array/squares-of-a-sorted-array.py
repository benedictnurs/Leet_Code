class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sol = deque()
        left = 0
        right = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                sol.appendleft(nums[left]**2)
                left += 1
            else:
                sol.appendleft(nums[right]**2)
                right -= 1
        
        return list(sol)