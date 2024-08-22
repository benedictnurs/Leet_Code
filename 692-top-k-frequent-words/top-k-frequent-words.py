class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        print(words)        
        heap = []
        for word,count in words.items():
            heapq.heappush(heap,(-count,word))
        
        print(heap)

        ans = []

        while k:
            val = heapq.heappop(heap)
            ans.append(val[1])
            k-=1
        return (ans)