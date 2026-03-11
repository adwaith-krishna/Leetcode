class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        l=0
        r=0

        leng=len(nums)
        for r in range(leng):
            if nums[r]!=val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1



        return l



a=Solution()
nums = [3,2,2,3]
val = 3
print(a.removeElement(nums,val))


nums = [0,1,2,2,3,0,4,2]
val = 2
print(a.removeElement(nums,val))