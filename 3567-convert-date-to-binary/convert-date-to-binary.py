class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst = (date.split("-"))
        ans = ""
        for i in lst:
            ans += "{0:b}".format(int(i)) + "-"
        return(ans[:-1])