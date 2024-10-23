class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sol = 0
        if len(arr) % 2 != 0:
            combo = len(arr)
        else:
            combo = len(arr) - 1

        for i in range(1, combo + 1, 2):
            for j in range(len(arr)-i+1):
                sol += sum(arr[j:j+i])
        return sol