class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        k=3
        n=len(s)
        # for i in range(k):
        #     if len(set(s[:k])) == k:
        #         count = 1

        for i in range(k,n+1):
            window = s[i-k:i]
            if len(set(window)) == k:
                count+=1




        return count


a=Solution()

s = "xyzzaz"
print(a.countGoodSubstrings(s))

s = "aababcabc"
print(a.countGoodSubstrings(s))


