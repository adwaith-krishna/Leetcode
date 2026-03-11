class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxvol=0
        pl=0
        pr=len(height)-1

        #print(height[3])
        while pl<pr:

            del_i=pr-pl
            m=min(height[pl],height[pr])
            mv=del_i*m
            if mv>maxvol:
                maxvol=mv

            if height[pl]<height[pr]:
                pl+=1
            elif height[pl]>height[pr]:
                pr-=1
            else:
                pl+=1

   

        return maxvol
        


a=Solution()
height = [1,8,6,2,5,4,8,3,7]
print(a.maxArea(height))