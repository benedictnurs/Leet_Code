"""
Loop from a -> target letter
For i and i is the target
While loop to keep increasing char starting from 97 -> wtv 
append everything to sol
reset loop val to a?
"""


class Solution:
    def stringSequence(self, target: str) -> List[str]:

        sol = []
        curr = ''

        for i in target:
            curr += 'a'
            sol.append(curr)
            while curr[-1] != i:
                curr = curr[:-1] + chr(ord(curr[-1]) + 1)
                sol.append(curr)
        return sol

            