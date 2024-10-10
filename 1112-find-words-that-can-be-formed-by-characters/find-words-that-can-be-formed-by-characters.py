class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sol = 0 
        hm = {}
        
        for i in set(chars):
            hm[i] = chars.count(i)
            
        for word in words:
            good = True
            for letter in set(word):
                if letter in hm:
                    if hm[letter] < (word.count(letter)):
                        good = False
                        break
                else:
                    good = False
                    break
            
            if good:
                sol += len(word)
        
        return(sol)
        
        