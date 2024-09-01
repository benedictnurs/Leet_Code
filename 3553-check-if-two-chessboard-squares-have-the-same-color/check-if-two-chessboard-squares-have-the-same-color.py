class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        alpha = list("abcdefgh")
        nums = list("12345678")
        seen = []
        
        coord1 = list(coordinate1)
        if alpha.index(coord1[0]) % 2 == 0:
            if nums.index(coord1[1]) % 2 == 0:
                seen.append("Black")
            else:
                seen.append("White")
        else:
            if nums.index(coord1[1]) % 2 == 0:
                seen.append("White")
            else:
                seen.append("Black")
        
        coord2 = list(coordinate2)
        if alpha.index(coord2[0]) % 2 == 0:
            if nums.index(coord2[1]) % 2 == 0:
                seen.append("Black")
            else:
                seen.append("White")
        else:
            if nums.index(coord2[1]) % 2 == 0:
                seen.append("White")
            else:
                seen.append("Black")
        
        return len(seen) != len(set(seen))