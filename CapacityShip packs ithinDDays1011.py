class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left,right=max(weights),sum(weights)

        while left<=right:
            current_load=0
            days_needed=1
            mid=(left+right)//2

            for num in weights:
                if current_load+num<=mid:
                    current_load=current_load+num
                else:
                    days_needed+=1
                    current_load=num
            if days_needed<=days:
                right=mid-1
            elif days_needed>days:
                left=mid+1
        
        return left
a=Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(a.shipWithinDays(weights,days))

weights = [3,2,2,4,1,4]
days = 3
print(a.shipWithinDays(weights,days))

weights = [1,2,3,1,1]
days = 4
print(a.shipWithinDays(weights,days))