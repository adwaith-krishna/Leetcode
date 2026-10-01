class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                print("ok")


        return nums



a=Solution()

nums = [1,2,3]
print(a.nextPermutation(nums))

nums = [3,2,1]
print(a.nextPermutation(nums))

nums = [1,1,5]
print(a.nextPermutation(nums))