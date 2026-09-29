class Solution:
    def isPalindrome(self, s: str) -> bool:
        res="".join(i.lower() for i in s if i.isalnum())
        if res==res[::-1]:
            return True
        else:
            return False