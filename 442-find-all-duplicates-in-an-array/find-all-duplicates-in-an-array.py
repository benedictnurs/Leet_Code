class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm = {}
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        
        sol = []

        for k, v in hm.items():
            print(k, v)
            if v == 2:
                sol.append(k)
                
        return sol