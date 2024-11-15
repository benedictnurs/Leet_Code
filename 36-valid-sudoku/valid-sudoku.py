class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate col
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[row])):
                if board[row][col] not in seen:
                    if board[row][col] != ".":                 
                        seen.add(board[row][col])
                else:
                    return False

        # Validate row
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[row])):
                if board[col][row] not in seen:
                    if board[col][row] != ".":                 
                        seen.add(board[col][row])
                else:
                    return False
        
        hm = {}
        nb = sum(board,[])
        count = 0
        curr = 0
        pos = 0
        matrix = 0
        hm = {}
        while curr < len(nb):
            sol_row = []
            while count < 3:
                if nb[curr] != ".":
                    sol_row.append(nb[curr])
                curr += 1
                count += 1
            pos += 1
            if pos not in hm:
                hm[pos] = [sol_row]
            else:
                hm[pos].append(sol_row)
            if pos == 3:
                pos = 0
            count = 0

        values = list(hm.values())
        for i in range(len(values)):
            for j in range(0, len(values[i]), 3):
                totals = sum(values[i][j:j+3],[])
                if (len(totals) != len(set(totals))) == True:
                    return False
                    
        return True