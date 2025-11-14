class Solution:
    def partitionLabels(self, s: str) -> List[int]: 
        hm = {}
        sol = []
        end = 0
        count = 0
        for n, i in enumerate(s):
            hm[i] = n

        for index, letter in enumerate(s):
            end = max(end, hm[letter])
            # print(index, letter, end)
            count += 1
            if index == end:
                sol.append(count)
                count = 0
        return sol