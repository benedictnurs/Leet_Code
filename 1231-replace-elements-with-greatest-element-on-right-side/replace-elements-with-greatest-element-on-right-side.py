class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        curr = 0
        sol = [-1]

        while n:
            curr = max(arr[n], curr)
            sol.append(curr)
            n -= 1
        return sol[::-1]