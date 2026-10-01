class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left,right=0,0
        maxcount=0
        count=0

        for right in range(len(nums)):
            if nums[right]==0:
                count+=1
            while count>k:

                if nums[left]==0:
                    count-=1
                left+=1
            if maxcount<right-left+1:
                maxcount=right-left+1

        return maxcount



a=Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(a.longestOnes(nums,k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(a.longestOnes(nums,k))
