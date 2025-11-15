class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        
        for word in strs:
            key = [0 for _ in range(26)]

            for letter in word:
                key[(ord(letter) - ord('a'))] += 1
            
            if tuple(key) not in hm:
                hm[tuple(key)] = [word]
            else:
                hm[tuple(key)].append(word)
        
        return list(hm.values())



