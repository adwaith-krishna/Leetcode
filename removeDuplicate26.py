class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # res=[]
        # for i in range(len(nums)):
        #     if nums[i] not in res:
        #         res.append(nums[i])
        # return res

        frst=0
        scnd=0
        temp=nums[0]
        for frnt in range(1,len(nums)):
            if nums[frst]==temp:
                frst+=1
            else:
                temp=nums[frst]
                scnd+=1
                nums[scnd]=nums[frst]


        return nums



        frst = 0

        for scnd in range(1, len(nums)):
            if nums[scnd] != nums[frst]:
                frst += 1
                nums[frst] = nums[scnd]

        return frst + 1


        # temp=0
        # frst=0
        # scnd=0
        # for i in range(len(nums)):
        #     if 

        


a=Solution()
nums = [1,1,2]
print(a.removeDuplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(a.removeDuplicates(nums))