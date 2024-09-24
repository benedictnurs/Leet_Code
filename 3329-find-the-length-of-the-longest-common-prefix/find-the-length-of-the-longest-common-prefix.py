class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen1 = set()
        seen2 = set()

        for num in arr1:
            prefix = str(num)
            for i in range(len(prefix) + 1):
                seen1.add(prefix[:i])

        for num in arr2:
            prefix = str(num)
            for i in range(len(prefix) + 1):
                seen2.add(prefix[:i])

        if seen1 & seen2:
            return len(sorted(seen1 & seen2, key = lambda x: len(x))[-1])

        return 0