class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #Time there + time Travelling
        #Travel is time spend travelling from index i to i+1 we start and house 0
        time = 0
        trv = travel 
        hm = {}

        for g in range(len(garbage)):
            if "G" in garbage[g]:
                if "G" not in hm:
                    hm["G"] = [garbage[g].count("G"), g]
                else:
                    hm["G"][0] += garbage[g].count("G")
                    hm["G"][1] = g
            if "P" in garbage[g]:
                if "P" not in hm:
                    hm["P"] = [garbage[g].count("P"), g]
                else:
                    hm["P"][0] += garbage[g].count("P")
                    hm["P"][1] = g
            if "M" in garbage[g]:
                if "M" not in hm:
                    hm["M"] = [garbage[g].count("M"), g]
                else:
                    hm["M"][0] += garbage[g].count("M")
                    hm["M"][1] = g

        if "P" in hm:
            count = hm["P"][0]
            index = hm["P"][1]
            time += (sum(trv[:index]) + count)
              
        if "G" in hm:
            count = hm["G"][0]
            index = hm["G"][1]
            time += (sum(trv[:index]) + count)

        if "M" in hm:
            count = hm["M"][0]
            index = hm["M"][1]
            time += (sum(trv[:index]) + count)

        print(time)
        return time



