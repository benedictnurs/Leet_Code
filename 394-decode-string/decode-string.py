class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            print(stack)
            if i != "]":
                stack.append(i)
            if i == "]":
                curr = ""
                while stack[-1] and stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(curr * int(num))
        print(stack)
        return "".join(stack)