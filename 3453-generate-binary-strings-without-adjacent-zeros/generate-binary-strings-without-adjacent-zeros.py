class Solution:
    def validStrings(self, n: int) -> List[str]:
        sol = []

        def backtrack(i, binary):
            if len(binary) == n:
                sol.append(binary)
                return
            
            backtrack(i+1, binary+"1")
            if binary and binary[-1] == "0":
                pass
            else:
                backtrack(i+1, binary+"0")


        backtrack(n,"")

        return sol

