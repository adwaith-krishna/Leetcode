class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
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
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(a.longestOnes(nums,k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(a.longestOnes(nums,k))
