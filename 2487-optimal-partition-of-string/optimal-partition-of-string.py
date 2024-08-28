class Solution:
    def partitionString(self, s: str) -> int:
        hm = {}
        s = list(s)
        current = []
        count = 0
        for i in s:
            if i not in current:
                current.append(i)
            else:
                count+=1
                print(current)
                current = [i]
        
        return (count) + 1