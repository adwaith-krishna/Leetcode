class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')
        # res=[1]*len(nums)
        # pl,pr=1,1
        # flag = False
        # rl,rr=0,0

        # res.append(nums[0])

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             res[i]=max(res[i],res[j]+1)

        # if max(res)>=3:
        #     return True     


        # return False
        # while not flag:
        #     if 


        # for i in range(1,len(nums)):
        #     res.append(nums[i])




        # while pr<len(nums):
        #     if nums[pr]>res[rr]:
        #         res.append(nums[pr])
        #         pr+=1
        #         rr+=1

        #     if nums[pr]<res[rr]:
        #         res.clear()
        #         res.append(nums[pr])
        #         pr+=1
        #         rr=0

        # return res


s=Solution()

nums = [1,2,3,4,5]
print(s.increasingTriplet(nums))

nums = [5,4,3,2,1]
print(s.increasingTriplet(nums))


nums = [2,1,5,0,4,6]
print(s.increasingTriplet(nums))

nums=[2,4,-2,-3]
print(s.increasingTriplet(nums))