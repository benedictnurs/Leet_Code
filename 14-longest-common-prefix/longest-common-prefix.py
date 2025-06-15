class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        first = strs[0]
        last = strs[-1]
        prefix = ""

        if first == last:
            return strs[0]
        for i in range(min(len(first), len(last))):
            print(first[i], last[i])
            if (first[i] == last[i]):
                prefix += first[i]
                print(prefix, "P")
            else:
                return prefix

        return prefix