from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        scount={}
        wincount=Counter()
        left, right = 0, 0
        scount = Counter(s1)
        
        while right<len(s2):
            wincount[s2[right]] += 1
            winsize=right-left+1
            if winsize>len(s1):
                wincount[s2[left]]-=1
                left+=1
            winsize=right-left+1
            if winsize==len(s1):

                if wincount==scount:
                    return True
            right+=1

        return False
        


a=Solution()
s1 = "ab"
s2 = "eidbaooo"
print(a.checkInclusion(s1,s2))

s1 = "ab"
s2 = "eidboaoo"
print(a.checkInclusion(s1,s2))