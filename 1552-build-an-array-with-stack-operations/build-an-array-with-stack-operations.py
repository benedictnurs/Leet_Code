class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        sol = []
        if target[-1] < n:
            for i in range(1, target[-1]+1):
                if i in target:
                    sol.append("Push")
                else:
                    sol.append("Push")
                    sol.append("Pop")
            return sol

        for i in range(1, n+1):
            if i in target:
                sol.append("Push")
            else:
                sol.append("Push")
                sol.append("Pop")
        return sol