class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # pl=0
        # pr=len(nums)

        # for i in range(len(nums)):

        # while pl<pr:
        #     if nums[pl]<nums[pr]:
        #         nums[pl],nums[pr]=nums[pr],nums[pl]


        largest=max(nums)
        cntArr = [0] * (largest+1)

        arr = nums.copy()
        
        for num in nums:
            cntArr[num] += 1

        for i in range(1, largest+1):
            cntArr[i] = cntArr[i-1] + cntArr[i]

        for i in range(len(arr) - 1, -1, -1):
            v = arr[i]
            nums[cntArr[v] - 1] = v
            cntArr[v] -= 1

        return nums



a=Solution()
nums = [2,0,2,1,1,0]
print(a.sortColors(nums))

nums = [2,0,1]
print(a.sortColors(nums))