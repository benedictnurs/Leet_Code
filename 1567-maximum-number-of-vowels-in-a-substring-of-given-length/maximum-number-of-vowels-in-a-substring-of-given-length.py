class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        maxx = count
        
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            maxx = max(count,maxx)

        return maxx
