class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        "abbaca"
        "aaca"
        "ca"
        """
        stack = []

        for i in s:
            stack.append(i)
            if len(stack) != 1 and i == stack[-2]:
               stack.pop()
               stack.pop()

        return("".join(stack))