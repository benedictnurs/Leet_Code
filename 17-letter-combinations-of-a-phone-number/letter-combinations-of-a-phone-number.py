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
    
        lists = [keyboard[i] for i in digits]
        sol = []

        for combo in list(product(*lists)):
            sol.append("".join(list(combo))) 

        return sol

