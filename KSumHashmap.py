class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:

        visit={}
        op=0

        for i in range(len(nums)):
            diff = k-nums[i]
            if diff in visit:
                op+=1

            visit[nums[i]]=i





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