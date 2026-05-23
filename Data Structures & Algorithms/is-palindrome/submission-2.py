class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = ""
        for i in s:
            if i.isalnum():
                z += i.lower()
        return z[::-1] == z