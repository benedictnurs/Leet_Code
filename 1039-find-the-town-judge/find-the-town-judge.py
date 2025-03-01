class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        isTrustedBy = {i: [] for i in range(1,n+1)}
        trustsSomeone = {i: False for i in range(1,n+1)}
        for edge in trust:
            k = edge[0]
            v = edge[1]
            isTrustedBy[v].append(k)
            trustsSomeone[k] = True

        for k,v in isTrustedBy.items():
            if trustsSomeone[k] == False and len(v) == n-1:
                return(k)

        return -1