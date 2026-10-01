class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        
        return res





a=Solution()


nums = [2,5,1,3,4,7]
n = 3
print(a.shuffle(nums,n))


nums = [1,2,3,4,4,3,2,1]
n = 4
print(a.shuffle(nums,n))

nums = [1,1,2,2]
n = 2
print(a.shuffle(nums,n))