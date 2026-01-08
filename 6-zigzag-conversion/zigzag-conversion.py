import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]
        sol = ""
        count = 0
        count_down = False

        for i in range(len(s)):
            matrix[count].append(s[i])
            if count_down == False and count < numRows - 1:
                count += 1
            if count_down == True:
                count -= 1
            if count > numRows - 2:
                count_down = True
            if count == 0:
                count_down = False

        
        for i in (matrix):
            sol += ("".join(i))
        
        return(sol)