class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board[0])
        col = len(board)

        # Validate col
        for c in range(col):
            seen = set()
            for r in range(row):
                if board[r][c] != ".":
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

        # Validate row
        for c in range(col):
            seen = set()
            for r in range(row):
                if board[c][r] != ".":
                    if board[c][r] in seen:
                        return False
                    seen.add(board[c][r])

        for square in range(0, 9, 3):
            tracker = []
            for c in range(9):
                seen = []
                for r in range(square, square + 3):
                    if board[c][r] != ".":
                        seen.append(board[c][r])
                tracker.append(seen)

            for item in range(0, 9, 3):
                mat = []
                for i in (tracker[item:item+3]):
                    mat.extend(i)
                if len(mat) != len(set(mat)):
                    return False
 
        return True
        