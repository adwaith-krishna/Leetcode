class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res=0
        for n in nums:
            res^=n
            
            
        return res
        


a=Solution()
nums = [2,2,3,2]
print(a.singleNumber(nums))

nums = [0,1,0,1,0,1,99]
print(a.singleNumber(nums))

