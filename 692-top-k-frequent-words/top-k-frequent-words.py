class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        heap = []
        for word,count in words.items():
            heapq.heappush(heap,(-count,word))
        

        ans = []

        while k:
            val = heapq.heappop(heap)
            ans.append(val[1])
            k-=1
        
        return (ans)