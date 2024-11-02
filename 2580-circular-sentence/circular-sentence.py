class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split()
        if len(lst) == 1:
            return sentence[-1] == sentence[0]
        if (lst[0][0] != lst[-1][-1]):
            return False
        for i in range(len(lst)+2-1):
            temp = (lst[i:i+2])
            if len(temp) == 2:
                one = temp[0]
                two = temp[1]
                if (one[-1] != two[0]):
                    return False
        return True
 