class Solution:
    def isPalindrome(self, x: int) -> bool:

        rev=0
        num=x
        sign=False
        if x<0:
            # sign=True
            return False
        x=abs(x)

        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if num==rev:
            return True
        return False





        # if sign==True:
        #     rev=-rev



a=Solution()
x = 121
print(a.isPalindrome(x))

x = -121
print(a.isPalindrome(x))

x = 10
print(a.isPalindrome(x))