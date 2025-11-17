class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        start = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                start = i
                break

        count = 0
        for i in range(start+1, len(nums)):
            if nums[i] == 1:
                if count < k:
                    return False
                count = 0
                continue
            count += 1


        return True