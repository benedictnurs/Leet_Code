class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) != 1 and i == "B" and stack[-2] == "A":
                stack.pop()
                stack.pop()
            if len(stack) != 1 and i == "D" and stack[-2] == "C":
                stack.pop()
                stack.pop()
        return len(stack)