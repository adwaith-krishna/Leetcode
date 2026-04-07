class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
        string=""
        for c in s:
            if c.isalnum():
                string += c
        string=string.lower()
        s=string
        string=string[::-1]
        if s==string:
            return True
        return False


 



a=Solution()

s = "A man, a plan, a canal: Panama"
print(a.isPalindrome(s))

s = "race a car"
print(a.isPalindrome(s))

s = " "
print(a.isPalindrome(s))