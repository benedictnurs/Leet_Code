class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        idx = []
        hm = {}

        for letter in pattern:
            idx.append(pattern.index(letter))
        
        for word in words:
            indexs = []
            for letter in word:
                indexs.append(word.index(letter))
            if tuple(indexs) not in hm:
                hm[tuple(indexs)] = [word]
            else:
                hm[tuple(indexs)].append(word)
        

        for pos, word in hm.items():
            if pos == tuple(idx):
                return(word)

        