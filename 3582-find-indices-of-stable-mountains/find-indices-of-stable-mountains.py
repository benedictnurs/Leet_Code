class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []

        for i in range(1,len(height)):
            if height[i-1] > threshold:
                ans.append(i)

        return ans

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution().stableMountains(nums, next(inputs))).replace(" ", ""), file=f)
exit(0)