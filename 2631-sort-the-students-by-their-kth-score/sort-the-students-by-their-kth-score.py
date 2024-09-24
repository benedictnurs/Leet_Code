class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key = lambda x: x[k], reverse = True) 

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution().sortTheStudents(nums, next(inputs))).replace(" ", ""), file=f)
exit(0)