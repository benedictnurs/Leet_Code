class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        count = 0
        for i in range(len(s)-1):
            print(s[i], s[i+1])
            if hm[s[i]] < hm[s[i+1]]:
                count -= hm[s[i]]
            else:
                count += hm[s[i]]
        return (count +  hm[s[-1]])
