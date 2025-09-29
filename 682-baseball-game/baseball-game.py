class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sol = 0
        for i in operations:
            if i not in ["+","D","C"]:
                stack.append(int(i))
                sol += int(i)
            elif i == "+":
                sol += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                sol += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif i == "C":
                sol -= stack[-1]
                stack.pop()
            print(stack, sol)
        return sol