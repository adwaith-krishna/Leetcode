class Solution:
	def sumOfCubes(self, a:int,b:int) -> int:
		sum=0

		for i in range(a,b+1):
			sum=sum+i**3

		return sum


s=Solution()
a=4
b=9
print(s.sumOfCubes(a,b))