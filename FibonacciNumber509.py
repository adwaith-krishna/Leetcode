class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
        


a=Solution()

n = 2
print(a.fib(n))

n = 3
print(a.fib(n))

n = 4
print(a.fib(n))