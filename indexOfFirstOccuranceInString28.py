class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        frst=0
        scnd=0
        res=0

        # for i in range(len(haystack)):
        #     if haystack[frst]==needle[scnd]:
        #         frst+=1
        #         scnd+=1
        #     else:
        #         scnd=0
        #         frst+=1


        # for i in range(len(haystack)):
        #     if haystack[frst]!=needle[scnd]:
        #         frst+=1
        #         scnd=0
        #     elif scnd<len(needle):
        #         scnd+=1
        #         frst+=1


        # print(haystack[frst])


        return haystack.find(needle)


        

a=Solution()
haystack = "sadbutsad"
needle = "sad"
print(a.strStr(haystack,needle))