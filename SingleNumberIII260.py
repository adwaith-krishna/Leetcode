class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        res=0
        for n in nums:
            res^=n

        return res



a=Solution()
nums = [1,2,1,3,2,5]
print(a.singleNumber(nums))


nums = [-1,0]
print(a.singleNumber(nums))

nums = [0,1]
print(a.singleNumber(nums))