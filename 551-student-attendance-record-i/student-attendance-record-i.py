class Solution:
    def checkRecord(self, s: str) -> bool:
        
        if s.count("A") >= 2:
            return False

        for i in range(len(s)-2):
            curr = s[i:i+3]
            if curr == "LLL":
                return False
        
        return True