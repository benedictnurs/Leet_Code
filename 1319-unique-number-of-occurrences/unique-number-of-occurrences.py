class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lst = Counter(arr)
        return len(lst.values()) == len(set(lst.values()))
