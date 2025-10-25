class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 0
        curr = 0
        total = 0

        for i in range(1, n+1):
            if i % 7 == 0:
                curr += 1
                total += curr
                monday += 1
                curr = monday
            else:
                curr += 1
                total += curr

        return(total)
            