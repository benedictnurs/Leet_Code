class Solution:
    def partitionString(self, s: str) -> int:
        current = []
        count = 0
        
        for i in s:
            if i not in current:
                current.append(i)
            else:
                count += 1
                current = [i]
        
        return count + 1