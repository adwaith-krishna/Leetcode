class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1

        # mid=(len(nums))//2
        # if nums[mid]==target:
        #     return mid
        # elif target<nums[mid]:
        #     for i in range(0,mid):
        #         if nums[i]==target:
        #             return i
        # elif target>nums[mid]:
        #     for i in range(mid,len(nums)):
        #         if nums[i]==target:
        #             return i
        # return -1



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
        return -1





a=Solution()


nums = [-1,0,3,5,9,12]
target = 9
print(a.search(nums,target))


nums = [-1,0,3,5,9,12]
target = 2
print(a.search(nums,target))