class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        for char in s:
            if char == "(":
                if count>0:
                    res.append(char)
                count+=1
            else:
                count-=1
                if count>0:
                    res.append(char)
        res = "".join(res)
        return res
        




a=Solution()
s = "(()())(())"
print(a.removeOuterParentheses(s))

s = "(()())(())(()(()))"
print(a.removeOuterParentheses(s))