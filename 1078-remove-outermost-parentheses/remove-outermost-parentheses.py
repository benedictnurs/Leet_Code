class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        sol = []

        for i in s:
            if i == "(":
                if stack:
                    sol.append("(")
                stack.append("(")
            else:
                stack.pop()
                if stack:
                    sol.append(")")
        
        return "".join(sol)