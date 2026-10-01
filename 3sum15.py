class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        
        for i in range(0,len(nums)-1):
            left = i+1
            right = len(nums)-1
            if i!=0:
                if nums[i]==nums[i-1]:
                        continue
            
            while left<right:
                if nums[left]+nums[right]+nums[i]==0:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:

                            right-=1
                elif nums[left]+nums[right]+nums[i]<0:
                    left+=1
                else:
                    right-=1

        return res


        

a=Solution()
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))

nums = [0,1,1]
print(a.threeSum(nums))

nums = [0,0,0]
print(a.threeSum(nums))