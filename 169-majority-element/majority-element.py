class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = Counter(nums)
        print(nums)
        heap = []
        for k,v in nums.items():
            heappush(heap,(-v,k))
        
        return (heappop(heap)[1])
