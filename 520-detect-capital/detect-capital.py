class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all letters are uppercase
        if word.isupper():
            return True
        # Check if all letters are lowercase
        elif word.islower():
            return True
        # Check if only the first letter is uppercase and the rest are lowercase
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
