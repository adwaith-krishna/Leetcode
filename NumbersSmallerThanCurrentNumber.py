class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
    	res=[]
    	for i in range(len(nums)):
    		count=0
    		for j in range(len(nums)):
    			if i==j:
    				pass
    			elif nums[j]<nums[i]:
    				count+=1

    		res.append(count)
    		
    		print(nums[i])
    	return res
        




a=Solution()

nums = [6,5,4,8]
#[2,1,0,3]
print(a.smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
#[0,0,0,0]
print(a.smallerNumbersThanCurrent(nums))

