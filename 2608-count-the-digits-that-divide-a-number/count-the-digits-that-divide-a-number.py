class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        nums = [int(i) for i in str(num)]

        for i in nums:
            if num % i == 0:
                count += 1
        
        return count