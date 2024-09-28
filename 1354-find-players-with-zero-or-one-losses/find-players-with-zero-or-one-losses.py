class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        flattened_list = list(chain(*matches))
        peeps = set(flattened_list)
        hm = {}
        noloss = []
        oneloss = []

        for i in matches:
            lose = i[1]
            if lose not in hm:
                hm[lose] = 1
            else:
                hm[lose] += 1

        for i in sorted(peeps):
            if i not in hm:
                noloss.append(i)
            if i in hm and hm[i] == 1:
                oneloss.append(i)

        return ([(noloss),(oneloss)])
