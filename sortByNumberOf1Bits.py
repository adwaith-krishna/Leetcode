class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        fres=[]
        res={}

        for i in range(len(arr)):
            res[arr[i]] = arr[i].bit_count()


        if len(set(res.values())) == 1:
            fres=list(res.keys())
            fres=sorted(fres)
        else:
            print("Values are different")


        

            items=list(res.items())
            sitems = sorted(items, key=lambda x: x[1])
            res = dict(sitems)
            print(res)
            fres=list(res.keys())

        # nums = [1, 2, 3, 4, 5]
        # result = [n.bit_count() for n in nums]
        # print(result)



        # num = 8
        # print(num.bit_length())
        return fres






a=Solution()
arr = [0,1,2,3,4,5,6,7,8]
print(a.sortByBits(arr))

arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(a.sortByBits(arr))