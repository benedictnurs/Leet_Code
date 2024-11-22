class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = float(inf)
        n2 = float(inf)
        
        for i in nums:
            if i <= n1:
                n1 = i
            elif i <= n2:
                n2 = i
            else:
                return True
        return False