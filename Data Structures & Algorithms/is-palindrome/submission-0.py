class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = ""
        for i in s:
            if i.isalnum():
                z += i
        return z.lower()[::-1] == z.lower()