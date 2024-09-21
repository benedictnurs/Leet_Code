class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        count = [0] * len(A)
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            count[i] = len(a & b)
        return count