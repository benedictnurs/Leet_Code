class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()
    
        count = 0 
        t = 0

        for p in players:
            while t < len(trainers) and p > trainers[t]:
                t += 1
            if t < len(trainers):
                count += 1
                t += 1
        
        return count