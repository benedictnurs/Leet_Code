class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = {}
        sol = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in hm:
                hm[groupSizes[i]] = [i]
            else:
                hm[groupSizes[i]].append(i)
        print(hm)

        for k,v in hm.items():
            for i in range(0, (len(v)), k):
                sol.append(v[i:i+k])
        return sol