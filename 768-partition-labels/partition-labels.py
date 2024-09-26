class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        sol = []

        for i in range(len(s)):
            hm[s[i]] = i
        
        maxs = 0
        count = 0
        for i in range(len(s)):
            maxs = max(maxs, hm[s[i]])
            count += 1
            if i == maxs:
                sol.append(count)
                count = 0
        return sol