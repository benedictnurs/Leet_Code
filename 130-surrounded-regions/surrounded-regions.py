class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def dfs(r, c):
            if r >= n or r < 0 or c >= m or c < 0 or board[r][c] != "O":
                return
            board[r][c] = "#"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for row in range(n):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][m-1] == "O":
                dfs(row, m-1)

        for col in range(m):
            if board[0][col] == "O":
                dfs(0, col)
            if board[n-1][col] == "O":
                dfs(n-1, col)

        for row in range(n):
            for col in range(m):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"
        return board