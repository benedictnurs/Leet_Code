class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            g = (gcd(len(str1),len(str2)))
            return("".join(list(str1+str2)[:g]))
        return ""