class Solution:
    def reverse(self, x: int) -> int:

        rev=0
        sign=False
        if x<0:
            sign=True
        x=abs(x)

        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10



        if sign==True:
            rev=-rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev


a=Solution()
x = 123
print(a.reverse(x))

x = -123
print(a.reverse(x))

x = 120
print(a.reverse(x))

x=1534236469
print(a.reverse(x))
