class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sentence = "".join(ch if ch.isalnum() or ch == " " else " " for ch in paragraph.lower())
        print(sentence)
        words = sentence.split()
        
        hm = {}

        for word in words:
            if word not in banned:
                hm[word] = words.count(word)
        
        return max(hm.items(), key=lambda item: item[1])[0] if hm else ""