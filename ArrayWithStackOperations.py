class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        res=[]
        for i in range(1,n+1):
            if res==target:
                break
            if i in target:
                stack.append("Push")
                res.append(i)
            else:
                stack.append("Push")
                stack.append("Pop")

        return stack


a=Solution()

target = [1,3]
n = 3
print(a.buildArray(target,n))

target = [1,2,3]
n = 3
print(a.buildArray(target,n))

target = [1,2]
n = 4
print(a.buildArray(target,n))