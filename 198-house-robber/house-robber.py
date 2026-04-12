class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        total = [nums[0], nums[1], 0]
        total[2] = nums[0] + nums[2]


        for i in range(3, len(nums)):
            print(nums[i])
            total.append(
            max(
                nums[i] + total[i-3],
                nums[i] + total[i-2]
            ))
        print(total)
        return max(total)