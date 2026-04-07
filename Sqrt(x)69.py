class Solution:
    def mySqrt(self, x: int) -> int:

        left=0
        right=x
        

        while left<=right:
            mid=(left+right)//2

            if mid*mid==x:
                return mid
            elif mid*mid < x:
                left=mid+1
            elif mid*mid>x:
                right=mid-1
        return right







a=Solution()


x = 4
print(a.mySqrt(x))

x = 8
print(a.mySqrt(x))