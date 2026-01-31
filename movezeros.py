class Solution:
    # def moveZeroes(self, nums: list[int]) -> None:
    #     pl=0
    #     pr=len(nums)

    #     leng=len(nums)
    #     # for i in range(0,leng):
    #     while pl<pr:
    #         if nums[pl]==0:
    #             elem=nums.pop(pl)
    #             nums.append(elem)
    #         pl+=1




    #     return nums



    def moveZeroes(self, nums: list[int]) -> None:
        l=0
        r=0

        leng=len(nums)
        for r in range(leng):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            




        return nums
        







s=Solution()

nums = [0,1,0,3,12]
print(s.moveZeroes(nums))

nums = [0,0,1]
print(s.moveZeroes(nums))



