class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sol = [True for i in range(len(l))]

        for index in range(len(l)):
            start = l[index]
            end = r[index] + 1
            lst = sorted(nums[start:end])
            diff = lst[1]-lst[0]

            for i in range(len(lst)-1):
                if (lst[i+1]-lst[i]) != diff:
                    sol[index] = False

                
        return (sol) 
        
