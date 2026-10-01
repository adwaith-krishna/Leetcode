class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        length=0

        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1

        for char, count in count.items():

            length=length+(count//2)*2

        if length<len(s):
            return length+1



        return length
    



a=Solution()

s = "abccccdd"
print(a.longestPalindrome(s))

s = "a"
print(a.longestPalindrome(s))
