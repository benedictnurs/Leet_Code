class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = Counter(s)
        print(hm)

        for k,v in hm.items():
            if v == 1:
                return s.index(k)
        
        return -1