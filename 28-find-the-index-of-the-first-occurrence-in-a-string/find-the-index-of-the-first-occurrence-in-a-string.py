class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = 0
        k = len(needle)
        for i in range(len(haystack)-k+1):
            print(haystack[i:i+k])
            if haystack[i:i+k] == needle:
                return i
        return -1