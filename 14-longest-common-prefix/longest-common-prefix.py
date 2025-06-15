class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        prefix = ""

        for i in range(min(len(first), len(last))):
            if (first[i] == last[i]):
                prefix += first[i]
            else:
                return prefix

        return prefix