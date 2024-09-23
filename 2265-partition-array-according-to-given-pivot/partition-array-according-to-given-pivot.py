class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sm = [i for i in nums if i < pivot]
        lg = [i for i in nums if i > pivot]
        eq = [i for i in nums if i == pivot]
        return(sm + eq + lg)