import heapq
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Max-heap to store the closest k elements
        max_heap = []
        
        # Iterate through each element in the array
        for num in arr:
            # Push negative absolute difference to simulate a max-heap
            heapq.heappush(max_heap, (-abs(num - x), -num))
            
            # If heap exceeds size k, remove the largest element
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Extract elements from heap and sort them
        result = sorted(-num for _, num in max_heap)
        
        return result
