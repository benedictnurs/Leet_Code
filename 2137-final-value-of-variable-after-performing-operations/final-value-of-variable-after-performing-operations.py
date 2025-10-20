class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sol = 0
        for i in operations:
            if "+" in i:
                sol += 1
            else:
                sol -= 1
        return sol