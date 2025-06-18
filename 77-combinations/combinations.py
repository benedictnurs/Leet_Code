class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        res = []


        def backtrack(start):
            if len(res) == k:
                if len(set(res)) == len(res):
                    sol.append(res[:])
                return
            print(res)

            for i in range(start, n+1):
                res.append(i)
                backtrack(i+1)
                res.pop()

        backtrack(1)
        return sol
