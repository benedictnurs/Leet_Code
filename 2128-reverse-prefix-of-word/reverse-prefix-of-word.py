class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        sol = ""
        stack = []
        end = 0
        for r in range(len(word)):
            if word[r] == ch and end == 0:
                end = r + 1
                break
                
        for l in range(end):
            stack.append(word[l])
        
        for i in range(len(stack)):
            sol += stack.pop()

        return sol + word[end:]