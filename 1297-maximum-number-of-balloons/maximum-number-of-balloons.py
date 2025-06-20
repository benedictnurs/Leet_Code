class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        seen = set()
        sol = float(inf)

        if len(text) < 5:
            return 0
        for k,v in count.items():
            print(k,v)
            if k in "baloon":
                seen.add(k)
                if k in "lo":
                    sol = min(v//2, sol)
                else:
                    sol = min(v, sol)

        if seen != set(list(str("baloon"))):
            return 0

        if sol != float(inf):
            return sol
        else:
            return 0