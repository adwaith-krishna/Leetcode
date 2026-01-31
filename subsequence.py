class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s)== 1 and len(t)==1 and s!=t:
            return False

        sp=0
        tp=0

        #for i in range(len(t)-1):
        while sp<len(s) and tp<len(t):

            if s[sp]==t[tp]:
                sp+=1
            tp+=1
        return sp == len(s)

        #print(len(s))


        # if sp==len(s)-1:

        #     return True
        # else:

        #     return False


        # setT = set(t)
        # listS = list(s)
        # is_contained= all(item in setT for item in listS)
        # return is_contained
    



a=Solution()


s = "abc"
t = "ahbgdc"
print(a.isSubsequence(s,t)) #true
s = "axc"
t = "ahbgdc"
print(a.isSubsequence(s,t)) #false
s = "acb"
t = "ahbgdc"
print(a.isSubsequence(s,t)) #false
s = "b"
t = "c"
print(a.isSubsequence(s,t)) #false
s = "bb"
t = "ahbgdc"
print(a.isSubsequence(s,t)) #false


