class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = 0
        k = len(needle)
        for i in range(len(haystack)-k+1):
            if (haystack[i:i+len(needle)]) == needle:
                return i
        return -1