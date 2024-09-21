class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        lst = sentence.split(" ")
        if len(lst) == 1:
            print(lst)
            return lst[0][-1] == lst[0][0]

        if lst[-1][-1] != lst[0][0]:
            return False
 
        l = 0
        for r in range(1, len(lst)):
            print(lst[l][-1] ,lst[r][0])
            if lst[l][-1] == lst[r][0]:
                print("YES")
            else:
                return False
            l+=1
        
        return True
