class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursion(n):
            if n == 1:
                return True
            elif n == 0 or n % 4 != 0: 
                return False

            return recursion(n//4)

        return recursion(n)