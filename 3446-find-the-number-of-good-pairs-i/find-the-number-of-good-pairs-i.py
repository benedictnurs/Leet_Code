class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        count = 0
        
        # Iterate through nums1 and nums2 to count valid pairs
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                # Check if nums1[i] is divisible by nums2[j] * k
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
                    
        return count