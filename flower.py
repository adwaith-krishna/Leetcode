
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    count=0
    flowerbed=[0]+flowerbed+[0]
    for i in range(1,len(flowerbed)-1):
        if(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
            flowerbed[i]=1
            count+=1

            if count>=n:
                return True

    return count>=n


f= [1,0,0,0,1]
n = 1
res=canPlaceFlowers(f,n)
print(res)

f= [1,0,0,0,1]
n = 2
res=canPlaceFlowers(f,n)
print(res)