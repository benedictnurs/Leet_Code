class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        ans = 0
        for person in s:
            if person == "E":
                count+=1
            else:
                count-=1
            ans = max(ans, count)
        return ans