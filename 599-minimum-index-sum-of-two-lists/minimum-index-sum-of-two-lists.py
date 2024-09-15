class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm = {}
        minimum = 0
        new = {}

        for i in range(len(list1)):
            hm[list1[i]] = [i]
            
        for i in range(len(list2)):
            if list2[i] in hm:
                hm[list2[i]].append(i)
            else:
                hm[list2[i]] = [i]
        print(hm)

        for k,v in hm.items():
            if len(v) == 2:
                minimum = min(minimum, sum(v))
                if sum(v) not in new:
                    new[sum(v)] = [k]
                else:
                    new[sum(v)].append(k)
        print(new)
        return new[min(new)]          
