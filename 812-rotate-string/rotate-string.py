class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        newStr = goal*2

        if len(s) != len(goal):
            return False
        if s in newStr:
            return True
        else:
            return False
        