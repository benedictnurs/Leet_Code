class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(" ")

        if lst[-1][-1] != lst[0][0]:
            return False
 
        l = 0
        for r in range(1, len(lst)):
            if lst[l][-1] != lst[r][0]:
                return False
            l+=1
        
        return True
