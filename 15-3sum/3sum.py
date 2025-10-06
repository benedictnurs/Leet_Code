class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for l in range(len(nums)-1):
            m, r = l+1, len(nums) - 1
            if l > 0 and nums[l] == nums[l-1]:
                continue

            while m < r:
                total =  nums[l] + nums[m] + nums[r] 
                if total == 0:
                    sol.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1
                    while nums[r] == nums[r+1] and m < r:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    m += 1

        return sol