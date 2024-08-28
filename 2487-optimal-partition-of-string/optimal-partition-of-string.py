class Solution:
    def partitionString(self, s: str) -> int:
        seen = []
        count = 0
        
        for i in s:
            if i not in seen:
                seen.append(i)
            else:
                count += 1
                seen = [i]
        
        return count + 1