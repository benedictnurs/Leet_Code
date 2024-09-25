class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sentence = "".join(ch if ch.isalnum() or ch == " " else " " for ch in paragraph.lower())
        words = sentence.split()
        
        hm = {}

        for word in words:
            if word not in banned:
                if word in hm:
                    hm[word] += 1
                else:
                    hm[word] = 1
        
        return max(hm.items(), key=lambda item: item[1])[0] if hm else ""