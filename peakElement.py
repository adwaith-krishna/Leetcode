class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2

            if nums[mid]<nums[mid + 1]:
                left=mid+1
            else:
                right=mid


        return left
        




a=Solution()

nums = [1,2,3,1]
print(a.findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(a.findPeakElement(nums))
