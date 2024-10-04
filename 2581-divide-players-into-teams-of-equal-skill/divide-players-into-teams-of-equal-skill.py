class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        teams = []
        sumVal = skill[l] + skill[r]

        while l < r:
            if skill[l] + skill[r] != sumVal:
                return -1
            teams.append(skill[l] * skill[r])
            l += 1
            r -= 1 

        return sum(teams)

        
