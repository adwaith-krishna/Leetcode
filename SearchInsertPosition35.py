class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
        for i in range(len(nums)):
            if nums[i]>target:
                return i
        return len(nums)




        left=0
        right=len(nums)-1
        

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
        return left

            

a=Solution()

nums = [1,3,5,6]
target = 5
print(a.searchInsert(nums,target))

nums = [1,3,5,6]
target = 2
print(a.searchInsert(nums,target))

nums = [1,3,5,6]
target = 7
print(a.searchInsert(nums,target))