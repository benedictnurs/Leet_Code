class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        #we want to create an array and find how many users were active 
        #at that time the index represents the unique times they visited
        #How many people visited once?
        hm = {}
        lst = k*[0]
        for log in logs:
            user_id = log[0]
            minute = log[1]
            if user_id in hm:
                hm[user_id].add(minute)
            else:
                hm[user_id] = {minute}   
        
        for log in hm:
            location = len(hm[log])-1
            lst[location]+=1

        return lst
