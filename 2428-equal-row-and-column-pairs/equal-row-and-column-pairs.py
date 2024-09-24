class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm = {}
        count = 0

        for i in grid:
            if tuple(i) not in hm:
                hm[tuple(i)] = grid.count(i)
        print(hm)

        for row in range(len(grid)):
            column = []
            for col in range(len(grid[0])):
                column.append(grid[col][row])
            
            print((column))

            if tuple(column) in hm:
                count += hm[tuple(column)]

        return count