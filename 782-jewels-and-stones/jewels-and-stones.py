class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = Counter(jewels)
        s = Counter(stones)
        count = 0
        print(j,s)

        for k in j:
            if k in s:
                count += s[k] 

        return count