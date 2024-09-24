class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        temp = []
        sol = []
        for i in image:
            temp.append(i[::-1])

        for i in temp:
            hold = []
            og = i[:]
            for j in range(len(og)):
                if og[j] == 1:
                    hold.append(0)
                else:
                    hold.append(1)
            sol.append(hold)

        return sol
