class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                s = stack.pop()
                if s == "(" and i == ")":
                    pass
                elif s == "[" and i == "]":
                    pass
                elif s == "{" and i == "}":
                    pass
                else:
                    return False
        if stack:
            return False

        return True