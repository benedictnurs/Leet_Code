class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sol = set(nums)


        for i in nums:
            sol.add(int((str(i)[::-1])))
        
        return len(sol)