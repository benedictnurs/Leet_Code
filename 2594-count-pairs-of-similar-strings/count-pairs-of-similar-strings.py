class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hm = {}
        count = 0

        for i in words:
            word = "".join(sorted(set(i)))
            print(word)
            if word in hm:
                count += hm[word]
                hm[word] += 1
                print(count)
            else:
                hm[word] = 1
        print(hm)

        return count
