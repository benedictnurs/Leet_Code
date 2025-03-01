class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for edge in edges:
            for e in edge:
                if e in seen:
                    return e
                seen.add(e)
            