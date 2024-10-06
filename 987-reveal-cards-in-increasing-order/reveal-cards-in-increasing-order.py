class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        sol = [0] * len(deck)
        q = deque(range(len(deck)))

        for card in deck:
            index = q.popleft()
            sol[index] = card

            if q:
                q.append(q.popleft())
        return (sol)