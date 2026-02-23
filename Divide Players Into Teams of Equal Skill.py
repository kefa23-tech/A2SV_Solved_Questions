class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        teams = []
        min_ = 0
        max_ = len(skill) -1

        while min_ < max_:
            team = (skill[min_] , skill[max_]) 

            if teams :
                if sum(teams[-1]) == sum(team):
                    teams.append(team)
                else:
                    return -1
            else:
                teams.append(team)
            min_+=1
            max_-=1
        ans = 0

        for i,j in teams:
            ans+=i*j
        return ans
        
