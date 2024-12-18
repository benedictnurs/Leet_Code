class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hm = {}
        count = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60

            if complement in hm:
                count += hm[complement]
            
            if remainder not in hm:
                hm[remainder] = 1
            else:
                hm[remainder] += 1
                
        return count
                