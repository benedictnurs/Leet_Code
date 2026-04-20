class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def findCenter(l, r):
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                length += 1
            print(length)
            return length


        
        for i in range(len(s)):
            count += findCenter(i, i)
            count += findCenter(i, i+1)
        
        return count