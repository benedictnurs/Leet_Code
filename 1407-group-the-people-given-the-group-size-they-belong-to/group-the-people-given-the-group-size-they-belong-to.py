class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = {}
        sol = []

        for i in range(len(groupSizes)):
            if groupSizes[i] not in hm:
                hm[groupSizes[i]] = [i]
            else:
                hm[groupSizes[i]].append(i)
        
        for k, num in hm.items():
            for i in range(0, len(num), k):
                sol.append(num[i:i+k])
        
        return (sol)

