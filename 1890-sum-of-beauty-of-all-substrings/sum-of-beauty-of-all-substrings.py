class Solution:
    def beautySum(self, s: str) -> int:
        sol = 0
        n = len(s)
        
        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                max_freq = max(freq.values())
                min_freq = min(freq.values())
                sol += max_freq - min_freq

        return sol