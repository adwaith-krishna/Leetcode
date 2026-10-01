class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:

        stack=[]
        res=prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                ind=stack.pop()
                res[ind]-=prices[i]
            stack.append(i)
        return res
        




a=Solution()

prices = [8,4,6,2,3]
print(a.finalPrices(prices))

prices = [1,2,3,4,5]
print(a.finalPrices(prices))

prices = [10,1,1,6]
print(a.finalPrices(prices))