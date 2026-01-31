def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    pro=1
    count=1
    pl=len(nums)-1

    prefix=[]
    #prefix[0]=nums[0]
    prefix.append(nums[0])
    for i in range(1,len(nums)):
        #prefix.append(nums[i])
        if count==i:
            continue
        else:
            val=prefix[i-1]*nums[i]
            prefix.append(val)
            count+=1







    return prefix


    # while pl>=0:
    #     for i in range(len(nums)):
    #         if count!=i:
    #             pro=pro*nums[i]
    #         #count+=1
    #         pl-=1

    
    # return pro



    # for i in range(len(nums)):
    #     if count!=i:
    #         pro=pro*nums[i]

    #     #count+=1
    #     pl-=1


    # return pro




nums = [1,2,3,4]
print(productExceptSelf(nums))

# nums = [-1,1,0,-3,3]
# print(productExceptSelf(nums))