class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        sol = []

        for q in queries:
            for d in dictionary:
                count = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        count += 1
                if count <= 2:
                    print(count)
                    sol.append(q)
                    break
        return(sol)