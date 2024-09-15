class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        #we want to create an array and find how many users were active 
        #at that time the index represents the unique times they visited
        #How many people visited once?
        hm = {}
        lst = k*[0]
        for user_id, minutes in logs:
            if user_id in hm:
                hm[user_id].add(minutes)
            else:
                hm[user_id] = {minutes}   
        
        for log in hm:
            location = len(hm[log])-1
            lst[location]+=1

        return lst
