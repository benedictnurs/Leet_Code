class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        sol = []
        res = []
        def backtrack(index):
            if len(res) == len(digits):
                sol.append("".join(res[:]))
                return
            
            current = combinations[digits[index]]

            for i in range(len(current)):
                res.append(current[i])
                backtrack(index + 1)
                res.pop()

        backtrack(0)
        return sol

            