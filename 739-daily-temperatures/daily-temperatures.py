class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = (temperatures[i], i)
            while stack and stack[-1][0] < curr[0]:
                val = stack.pop()
                diff = i - val[1]
                sol[val[1]] = diff
            stack.append(curr)
        return sol
