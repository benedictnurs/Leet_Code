class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sol = ""
        l = 0

        for r in spaces:
            sol += (s[l:r] + " ") 
            l = r

        return (sol + s[l:])