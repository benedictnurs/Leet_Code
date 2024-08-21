import collections
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        lst = Counter(s)
        heap = []
        ans = ""

        for key,val in lst.items():
            heapq.heappush(heap,(-val,key))
        
        while heap:
            freq, char = heapq.heappop(heap)
            ans += char * (-freq)
        
        return ans
                