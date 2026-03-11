# import math

# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     snum=sorted(nums)
#     pl=0
#     pr=len(snum)-1
#     sum=0
#     res=[]
#     # for i in range(leng):
#     #     sum=pr+pl
#     #     if sum==target:
#     #         break
#     #     elif sum<target:
#     #         pr=pr+1
#     #     elif sum>target:
#     #         pl=pl+1

#     while pl<pr:
#         sum=snum[pr]+snum[pl]
#         if sum>target:
#             pr-=1
#         elif sum<target:
#             pl+=1
#         elif sum==target:
#             ele1=snum[pl]
#             ele2=snum[pr]

#             f=nums.index(ele1)
#             b=nums.index(ele2)
#             res.append(f)
#             res.append(b)
#             return res

#             #return ele2
#             # res.append(pl)
#             # res.append(pr)
#             # return res



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        visit={}

        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in visit:
                return visit[diff],i

            visit[nums[i]]=i




        

        # pl=0
        # pr=len(nums)-1
        # res=[]

        # while pl<pr:
        #     sum=nums[pl]+nums[pr]
        #     if sum<target:
        #         pl+=1
        #     elif sum>target:
        #         pr-=1
        #     elif sum==target:
                
        #         break
        # print(pl)
        # print(pr)


        # #return res.append([pl,pr])
        # return nums

    

a=Solution()

num = [2,7,11,15]
tar = 9
print(a.twoSum(num,tar))

num = [3,2,4]
tar = 6      
print(a.twoSum(num,tar))

num = [3,3]
tar = 6
print(a.twoSum(num,tar))