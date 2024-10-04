class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0 
        prev = 0 

        for lasers in bank:
            curr = lasers.count("1")
            if curr:
                count += prev * curr
                prev = curr
        
        return count
