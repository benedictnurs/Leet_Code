class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter(list(s1))
        k = len(s1)

        for i in range(len(s2)-k+1):
            if (Counter(list(s2[i:i+k])) == window):
                return True

        return False



