class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [i.lower() for i in s if i.isalnum()]
        return lst == lst[::-1]