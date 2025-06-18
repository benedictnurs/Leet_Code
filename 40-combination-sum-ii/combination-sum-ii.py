class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []
        count = Counter(candidates)
        def backtrack(current):
            if current == target:
                arr = sorted(res[:])
                if arr not in sol:
                    sol.append(arr)
                return
            if current > target:
                return
            
            for i in count:
                if count[i] > 0:
                    res.append(i)
                    count[i] -= 1
                    backtrack(current+i)

                    count[i] += 1
                    res.pop()

        backtrack(0)
        return sol
