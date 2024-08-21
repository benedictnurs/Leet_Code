class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for i in operations:
            if i.lstrip('-').isdigit():
                ans.append(int(i))
            elif i == "C":
                ans.pop()
            elif i == "D":
                doub = ans[-1] * 2
                ans.append(doub)
            elif i == "+":
                add = ans[-1] + ans[-2]
                ans.append(add)

        return sum(ans)
