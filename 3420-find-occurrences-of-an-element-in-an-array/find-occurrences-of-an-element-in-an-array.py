class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        hm = {}
        sol = []
        seenOrder = 1

        for i in range(len(nums)):
            if nums[i] == x:
                hm[seenOrder] = i
                seenOrder += 1

        for q in queries:
            if q in hm:
                sol.append(hm[q])
            else:
                sol.append(-1)
        print(sol)
        return sol

