class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left,right=0,0
        sum=0
        minlen=float('inf')
        for right in range(len(nums)):
            sum += nums[right]


            while sum>=target:  
                minlen=min(minlen,right-left+1)
                sum -= nums[left]
                left+=1
        if minlen<=len(nums):
            return minlen
        else:
            return 0




        




a=Solution()
target = 7
nums = [2,3,1,2,4,3]
print(a.minSubArrayLen(target,nums))

target = 4
nums = [1,4,4]
print(a.minSubArrayLen(target,nums))

target = 11
nums = [1,1,1,1,1,1,1,1]
print(a.minSubArrayLen(target,nums))

nums = [5,1,3,5,10,7,4,9,2,8]
target = 15
print(a.minSubArrayLen(target,nums))