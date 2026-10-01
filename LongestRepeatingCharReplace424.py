class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right=0,0
        freq={}
        maxlen=0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while (right-left+1)-max(freq.values())>k:
                freq[s[left]]-=1
                left+=1
            maxlen=max(right-left+1,maxlen)
        return maxlen



        




a=Solution()
s = "ABAB"
k = 2
print(a.characterReplacement(s,k))

s = "AABABBA"
k = 1
print(a.characterReplacement(s,k))
