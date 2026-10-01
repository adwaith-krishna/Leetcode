class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        dupli=-1
        miss=-1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
               dupli=nums[i]

        num = set(nums)
        print(num)
        for i in range(1,len(nums)+1):
            if i not in num:
                miss = i
                break
        
        return [dupli, miss]






a=Solution()

nums = [1,2,2,4]
print(a.findErrorNums(nums))

nums = [1,1]
print(a.findErrorNums(nums))
