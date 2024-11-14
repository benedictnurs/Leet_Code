class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = ""
        idx = 0

        while max(len(word1), len(word2)) != idx:
            if len(word1) > idx:
                sol += word1[idx]
            if len(word2) > idx:
                sol += word2[idx]
            idx += 1
        return (sol)