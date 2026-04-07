class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for n in nums:
            res^=n
            

        return res
        


a=Solution()
nums = [2,2,1]
print(a.singleNumber(nums))

nums = [4,1,2,1,2]
print(a.singleNumber(nums))

nums = [1]
print(a.singleNumber(nums))