class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        


        return max(count, key=count.get)




a=Solution()

nums = [3,2,3]
print(a.majorityElement(nums))


nums = [2,2,1,1,1,2,2]
print(a.majorityElement(nums))