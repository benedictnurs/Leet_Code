class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        start = image[sr][sc]
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or image[row][col] == color or image[row][col] != start:
                return
    
            image[row][col] = color
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        
        dfs(sr, sc)
        return (image)
