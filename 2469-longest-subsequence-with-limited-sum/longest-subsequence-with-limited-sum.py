class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sol = []


        for q in queries:
            count = 0
            val = 0
            for num in nums:
                if val + num <= q:
                    val += num
                    count += 1
                else:
                    break
            sol.append(count)
            q -= 1
        
        return sol
            

