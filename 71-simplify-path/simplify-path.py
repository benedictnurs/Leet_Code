class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = (path.split('/'))
        stack = []

        for d in directories:
            if d == "" or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return ('/' + '/'.join(stack))