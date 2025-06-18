class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sol = []
        res = []
        count = Counter(tiles)

        def backtrack():
            if res:
                sol.append(res[:])

            for i in count:
                if count[i] > 0:
                    res.append(i)
                    count[i] -= 1
                    backtrack()
                    count[i] += 1
                    res.pop()

        backtrack()
        return len(sol)