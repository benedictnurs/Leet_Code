class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            count = 0
            current = chars[read]
            while read < n and current == chars[read]:
                count += 1
                read += 1

            chars[write] = current
            write += 1

            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1

        return write