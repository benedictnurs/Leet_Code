class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count the frequency of each character in s
        s_count = Counter(s)
        result = []

        # Add characters from `order` in the specified order
        for char in order:
            if char in s_count:
                result.append(char * s_count[char])
                del s_count[char]

        # Add remaining characters that were not in `order`
        for char, count in s_count.items():
            result.append(char * count)

        return ''.join(result)