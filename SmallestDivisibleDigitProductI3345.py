class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        prod=1
        for digit in str(n):
            prod=prod*int(digit)

        if prod%t==0:
            return n
        else:
            return self.smallestNumber(n+1,t)
        

        



a=Solution()

n = 10
t = 2
print(a.smallestNumber(n,t))

n = 15
t = 3
print(a.smallestNumber(n,t))