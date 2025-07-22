class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = (list(s))
        l, r = 0, len(lst)-1

        while l < r:
            if lst[l].lower() == lst[r].lower():
                l += 1
                r -= 1
            elif lst[l].isalnum() == False:
                l += 1
            elif lst[r].isalnum() == False:
                r -= 1
            else:
                return False
        
        return True

