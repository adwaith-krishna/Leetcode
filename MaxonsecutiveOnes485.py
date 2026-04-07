class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        maxcount=0
        for i in range(len(nums)):
            if nums[i]!=1:
                if maxcount<count:
                    maxcount=count
                count=0
            else:
                count+=1

        if maxcount<=count:
            maxcount=count

        return maxcount



a=Solution()
nums = [1,1,0,1,1,1]
print(a.findMaxConsecutiveOnes(nums))

nums = [1,0,1,1,0,1]
print(a.findMaxConsecutiveOnes(nums))
