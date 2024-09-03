class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sol = "".join(str(ord(i) - 96) for i in s)

        while k:
            a = sum([int(i) for i in sol])
            sol = ""
            sol += str(a)
            k -= 1
        
        return int(sol)