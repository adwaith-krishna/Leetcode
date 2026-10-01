class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=[]
        hashmap={}
        n=len(nums)
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

        for i in range(1,n+1):
            if i not in hashmap:
                res.append(i)

        print(hashmap)

        return res


a=Solution()

nums = [4,3,2,7,8,2,3,1]
print(a.findDisappearedNumbers(nums))

nums = [1,1]
print(a.findDisappearedNumbers(nums))