class Solution:
    def pivotInteger(self, n: int) -> int:
        right = sum([i for i in range(1,n+1)])
        left = 0
        

        for i in range(1, n+1):
            left += i
            if left == right:
                return i
            right -= i
        return -1