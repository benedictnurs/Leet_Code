class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sol = []

        for word in words:
            appn = True
            for letter in word:
                if letter not in allowed:
                    appn = False
            if appn == True:
                sol.append(word)

        return len(sol)