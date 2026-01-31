import math

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    snum=sorted(nums)
    pl=0
    pr=len(snum)-1
    sum=0
    res=[]
    # for i in range(leng):
    #     sum=pr+pl
    #     if sum==target:
    #         break
    #     elif sum<target:
    #         pr=pr+1
    #     elif sum>target:
    #         pl=pl+1

    while pl<pr:
        sum=snum[pr]+snum[pl]
        if sum>target:
            pr-=1
        elif sum<target:
            pl+=1
        elif sum==target:
            ele1=snum[pl]
            ele2=snum[pr]

            f=nums.index(ele1)
            b=nums.index(ele2)
            res.append(f)
            res.append(b)
            return res

            #return ele2
            # res.append(pl)
            # res.append(pr)
            # return res
    


num = [2,7,11,15]
tar = 9
print(twoSum(num,tar))

num = [3,2,4]
tar = 6      
print(twoSum(num,tar))

nums = [3,3]
tar = 6
print(twoSum(num,tar))