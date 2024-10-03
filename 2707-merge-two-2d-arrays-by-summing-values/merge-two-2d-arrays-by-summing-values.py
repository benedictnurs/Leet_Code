class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hm = {}
        sol = []

        for i in nums1:
            if i[0] not in hm:
                hm[i[0]] = [i[1]]
            else:
                hm[i[0]].append(i[1])
        for i in nums2:
            if i[0] not in hm:
                hm[i[0]] = [i[1]]
            else:
                hm[i[0]].append(i[1])
        
        new = (dict(sorted(hm.items(),key=lambda x: x[0])))

        for k,v in new.items():
            sol.append([k, sum(v)])

        return sol
