class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        sol = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                print(count)
                sol = max(sol,count)
            else:
                count = 0
        
        print(sol)
        return sol
