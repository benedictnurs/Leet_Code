class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)
        new_code = code*2
        n = len(code)
        sol = []
        if k > 0:
            for i in range(n):
                sol.append(sum(new_code[i+1 : i+1 + k]))
        else:
            for i in range(n):
                sol.append(sum(new_code[n + i + k : n + i]))
        return sol