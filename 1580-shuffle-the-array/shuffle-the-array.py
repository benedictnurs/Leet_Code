class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        sol = []


        for i,j in zip(arr1,arr2):
            sol.append(i)
            sol.append(j)
        return (sol)