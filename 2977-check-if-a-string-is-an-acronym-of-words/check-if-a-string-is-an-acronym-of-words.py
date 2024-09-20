class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        comp = ""
        for word in words:
            first = list(word)[0]
            comp += first
        return comp == s