class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # buy=min(prices)
        # largest=buy
        # spos=prices.index(buy)
        # for num in prices[spos:]:
        #     if num > largest:
        #         largest=num

        # return largest-buy

        minprice=prices[0]
        maxprofit=0
        for num in prices:
            if num<minprice:
                minprice=num
            else:
                profit=num-minprice
                if profit>maxprofit:
                    maxprofit=profit



        return maxprofit


        


        
   



a=Solution()
prices = [7,1,5,3,6,4]
print(a.maxProfit(prices))

prices = [7,6,4,3,1]
print(a.maxProfit(prices))

prices = [2,4,1]
print(a.maxProfit(prices))
#2