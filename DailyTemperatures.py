class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        n=len(temperatures)
        res=[0]*n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind=stack.pop()
                res[ind]=i-ind
            stack.append(i)
        return res



a=Solution()

temperatures = [73,74,75,71,69,72,76,73]
print(a.dailyTemperatures(temperatures))

temperatures = [30,40,50,60]
print(a.dailyTemperatures(temperatures))

temperatures = [30,60,90]
print(a.dailyTemperatures(temperatures))