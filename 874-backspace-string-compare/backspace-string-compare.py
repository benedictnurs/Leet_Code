class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = []

        for i in s:
            sl.append(i)

            if i == "#" and len(sl) != 1:
                sl.pop()
                sl.pop()

        tl = []

        for i in t:
            tl.append(i)

            if i == "#" and len(tl) != 1:
                tl.pop()
                tl.pop()
        return ( list(filter(lambda x: x != "#", sl)) == list(filter(lambda x: x != "#", tl)))
