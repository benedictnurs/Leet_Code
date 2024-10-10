class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        l1 = []

        for i in s:
            if i == '#':
                if l1:
                    l1.pop()
            
            else:
                l1.append(i)

        l2 = []

        for j in t:
            if j == '#':
                if l2:
                    l2.pop()

            else:
                l2.append(j)

        if l1 == l2:
            return True
        
        return False
        