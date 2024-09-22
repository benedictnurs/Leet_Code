class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s = set(bannedWords)
        count = 0 

        for i in message:
            if i in s:
                count+=1
            if count > 1:
                return True