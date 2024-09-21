class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        result = ""

        for char in order:
            if char in s_count:
                result += (char * s_count[char])
                del s_count[char]

        for char, count in s_count.items():
            result += (char * count)

        return result