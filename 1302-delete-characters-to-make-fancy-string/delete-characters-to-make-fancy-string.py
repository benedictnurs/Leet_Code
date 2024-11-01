class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for i in s:
            if len(stack) >= 2 and stack[-1] == i and i == stack[-2]:
                pass
            else:
                stack.append(i)
        
        return "".join(stack)
        