class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        total = []
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
            
            count = 0
            for i in hm.values():
                if i == 2:
                    count += 1
            total.append(count)
            
        return total         

