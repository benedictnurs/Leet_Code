class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [char for char in s if char in "AEIOUaeiou"]
        vowels.sort()

        lst = list(s)
        vowel_index = 0
        
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                lst[i] = vowels[vowel_index]
                vowel_index += 1
        
        return "".join(lst)