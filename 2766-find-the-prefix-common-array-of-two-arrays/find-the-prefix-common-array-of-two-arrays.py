class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        total = [0]*len(A)
        hm = {}

        for i in range(len(A)):
            if A[i] not in hm:
                hm[A[i]] = 1
            elif A[i] in hm:
                hm[A[i]] += 1
 
            if B[i] not in hm:
                hm[B[i]] = 1  
            elif B[i] in hm:
                hm[B[i]] += 1
            
            count = list(hm.values()).count(2)
            total[i] = count
            
        return total         

