class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        op=0
        pl=0
        pr=len(nums)-1
        nums=sorted(nums)
        print(nums)

        while pl<pr:
            sum=0
            sum=nums[pl]+nums[pr]
            if sum==k:
                op+=1
                pl+=1
                pr-=1
            elif sum<k:
                pl+=1
            elif sum>k:
                pr-=1




        return op




a=Solution()
nums = [1,2,3,4]
k = 5
print(a.maxOperations(nums,k))

nums = [3,1,3,4,3]
k = 6
print(a.maxOperations(nums,k))

nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
print(a.maxOperations(nums,k))