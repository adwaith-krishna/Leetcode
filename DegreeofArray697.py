class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        deg = max(count.values())
        return deg
        



a=Solution()
nums = [1,2,2,3,1,4,2]
print(a.findShortestSubArray(nums))

nums = [1,2,2,3,1]
print(a.findShortestSubArray(nums))