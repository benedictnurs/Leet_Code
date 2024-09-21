class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort by the number of 1's in the binary representation, then by numeric value
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        return arr