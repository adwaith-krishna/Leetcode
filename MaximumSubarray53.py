class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res=nums[0]
        maxEnd=nums[0]
        for i in range(1,len(nums)):
            maxEnd=nums[i]+maxEnd
            maxEnd=max(maxEnd,nums[i])
            res=max(maxEnd,res)
        

        return res




a=Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(a.maxSubArray(nums))

nums = [1]
print(a.maxSubArray(nums))

nums = [5,4,-1,7,8]
print(a.maxSubArray(nums))