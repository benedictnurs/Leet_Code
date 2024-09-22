class Solution:
    def stringHash(self, s: str, k: int) -> str:
        lst = []
        sol = ""
        alph = {}


        for i in range(0, len(s), k):
            lst.append(s[i:i+k])

        for word in range(len(lst)):
            numVal = 0
            for letter in lst[word]:
                numVal += (ord(letter)-97)
            sol += chr((numVal%26)+97)
            
            print(numVal%26, numVal)
        return sol



