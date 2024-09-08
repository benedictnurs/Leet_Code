class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans = ""
        for i in date.split("-"):
            ans += "{0:b}".format(int(i)) + "-"
        return(ans[:-1])