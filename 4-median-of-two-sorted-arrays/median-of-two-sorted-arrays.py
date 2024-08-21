class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        total = len(merge)

        if total % 2 == 1:
            return float(merge[total//2])
        else:
            left = merge[total//2 - 1 ]
            right = merge[total // 2]
            return (right + left)/2
