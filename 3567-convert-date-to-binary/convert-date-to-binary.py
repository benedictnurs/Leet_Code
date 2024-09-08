class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst = (date.split("-"))
        print(lst)
        ans = ""
        for i in lst:
            print("{0:b}".format(int(i)))
            ans += "{0:b}".format(int(i)) + "-"

        return(ans[:-1])