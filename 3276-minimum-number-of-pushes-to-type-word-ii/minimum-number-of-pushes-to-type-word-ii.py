class Solution:
    def minimumPushes(self, word: str) -> int:
        hm = {}

        counts = Counter(list(word))
        sol = 0
        mapping = (counts.most_common())
        curr = 1
        mapped = 1
        for i in mapping:
            if curr >= 9:
                curr = 1
                mapped += 1
            print(curr)
            hm[i[0]] = mapped
            curr += 1
        
        print(hm)



        for letter, count in counts.items():
            sol += (hm[letter]*count)

        return sol