class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        last=""
        check = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char=="(" or char=="[" or char=="{":
                stack.append(char)
            else:
                if not stack:
                    return False
                top=stack.pop()

                if char==")" and top!="(":
                    return False
                if char=="]" and top!="[":
                    return False
                if char=="}" and top!="{":
                    return False



        if not stack:
            return True
        return False




        #return stack


a=Solution()

s = "()"
print(a.isValid(s))

s = "()[]{}"
print(a.isValid(s))

s = "(]"
print(a.isValid(s))

s = "([])"
print(a.isValid(s))

s= "["
print(a.isValid(s))