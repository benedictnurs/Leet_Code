class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sol = 0
        for i in tokens:
            if i not in ["+","-","/","*"]:
                stack.append(i)

            if i in ["+","-","/","*"]:
                if len(stack) >= 2:
                    num1, num2 = int(stack[-1]), int(stack[-2])
                    stack.pop()
                    stack.pop()


                    if i == "+":
                        stack.append(num1 + num2)
                    elif i == "-":
                        stack.append(num2 - num1)
                    elif i == "/":
                        stack.append(num2 / num1)
                    elif i == "*":
                        stack.append(num1 * num2)

        return int(stack[0])
