class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"[":"]", "(":")", "{":"}"}
        stack = []

        for i in s:
            if i in pairs:
                stack.append(i)
            elif i in pairs.values():
                if not stack:
                    return False 
                peek = stack.pop()
                if pairs[peek] != i:
                    return False
                    
        return not stack