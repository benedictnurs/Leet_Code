class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        sol = []

        for i in image:
            hold = []
            for j in i[::-1]:
                if j == 1:
                    hold.append(0)
                if j == 0:
                    hold.append(1)
            sol.append(hold)

        return sol
