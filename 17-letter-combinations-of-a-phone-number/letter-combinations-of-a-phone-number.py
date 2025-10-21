class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
    
        sol = []
        res = []

        def backtrack(index):
            if index == len(digits):
                sol.append("".join(res[:]))
                return

            letters = keyboard[digits[index]]
            for i in letters:
                res.append(i)
                backtrack(index+1)
                res.pop()
            return
        
        backtrack(0)
        return (sol)
