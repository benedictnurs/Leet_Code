class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        nums = [i for i in str(num)]
        curr = nums[:k]
        if num % int("".join(curr)) == 0:
            count += 1


        for i in range(k,len(nums)):
            curr.pop(0)
            curr.append(nums[i])
            if int("".join(curr)) != 0 and num % int("".join(curr)) == 0:
                count += 1

        return count