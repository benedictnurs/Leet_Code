class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Create a counter for s1 and for the first window in s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        
        # Slide the window over s2
        for i in range(len(s1), len(s2)):
            if s1_count == window_count:
                return True
            
            # Update the window by removing the count of the outgoing character
            window_count[s2[i - len(s1)]] -= 1
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # Add the count of the incoming character
            window_count[s2[i]] += 1
        
        # Final check for the last window
        return s1_count == window_count