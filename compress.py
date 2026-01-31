class Solution:
    def compress(self, chars: list[str]) -> int:
        if chars is None:
            return chars
        pl=0
        pr=0
        leng=len(chars)
        while pr<leng:
            curchar=chars[pr]
            count=0
            while pr<leng and curchar==chars[pr]:
                pr+=1
                count+=1
            chars[pl]=curchar
            pl+=1
            if count>1:
                for char in str(count):
                    chars[pl]=char
                    pl+=1
        return chars[:pl]
        


s=Solution()
chars = ["a","a","b","b","c","c","c"]
gg=s.compress(chars)
print(gg)



chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
gg=s.compress(chars)
print(gg)

chars=["a"]

gg=s.compress(chars)
print(gg)