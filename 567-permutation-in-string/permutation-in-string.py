class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        counts = Counter(s1)

        for i in range(len(s2)-k+1):
            window = Counter(s2[i:i+k])
            if (window == counts) == True:
                return True
        return False
