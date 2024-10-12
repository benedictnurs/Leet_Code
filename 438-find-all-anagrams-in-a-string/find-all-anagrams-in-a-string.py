from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Edge case: if p is longer than s, there can't be any anagrams
        if len(p) > len(s):
            return []
        
        # Initialize variables
        p_count = Counter(p)  # Frequency count of characters in p
        s_count = Counter()   # Frequency count for current window in s
        k = len(p)            # Length of p
        sol = []              # List to store start indices of anagrams
        
        # Slide the window over s
        for i in range(len(s)):
            # Add the current character to the window
            s_count[s[i]] += 1
            
            # Remove the leftmost character if the window size exceeds p
            if i >= k:
                if s_count[s[i - k]] == 1:
                    del s_count[s[i - k]]
                else:
                    s_count[s[i - k]] -= 1
            
            # Compare the frequency count of the current window with p's frequency
            if s_count == p_count:
                sol.append(i - k + 1)
        
        return sol
