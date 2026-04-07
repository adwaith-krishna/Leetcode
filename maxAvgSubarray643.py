class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum=0
        n=len(nums)
        
        for i in range(k):
            sum=sum+nums[i]
        maxAvg=sum/k

        for i in range(k,n):
            sum=sum+nums[i]
            sum=sum-nums[i-k]
            avg=sum/k
            maxAvg=max(avg,maxAvg)



        return maxAvg
        






a=Solution()

nums = [1,12,-5,-6,50,3]
k = 4
#12.75000
print(a.findMaxAverage(nums,k))

nums = [5]
k = 1
print(a.findMaxAverage(nums,k))