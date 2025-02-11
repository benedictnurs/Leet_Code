class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        end_idx, end = len(part), list(part)

        for i in range(len(s)):
            stack.append(s[i])
            while (stack[-end_idx:]) == end:
                for i in range(len(end)):
                    stack.pop()

        return ("".join(stack))