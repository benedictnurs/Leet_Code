class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sol = ""
        for i in s:
            sol+=(str((ord(i))-96))

        while k:
            a = sum([int(i) for i in sol])
            sol = ""
            sol += str(a)
            k -= 1
        
        return (int(sol))