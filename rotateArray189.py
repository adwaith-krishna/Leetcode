class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # frst=0
        # scnd=len(nums)-1
        # count=1
        # while count<=k:
        #     nums=[nums[scnd]]+nums
        #     scnd-=1
        #     count+=1
        k=k%len(nums)


        nums = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]




        print(nums)


        


a=Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(a.rotate(nums,k))

nums = [-1,-100,3,99]
k = 2
print(a.rotate(nums,k))

