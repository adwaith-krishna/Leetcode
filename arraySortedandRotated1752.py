class Solution:
    def check(self, nums: list[int]) -> bool:
        n=len(nums)
        nums=nums+nums
        count=1


        for i in range(len(nums)-1):
            if count==n:
                return True

            if nums[i]>nums[i+1]:
                count=1
            else:
                count+=1

        return False

                
        







a=Solution()
nums = [3,4,5,1,2]
print(a.check(nums))

nums = [2,1,3,4]
print(a.check(nums))

nums=[1,2,3]
print(a.check(nums))