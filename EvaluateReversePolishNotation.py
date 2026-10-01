class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        signs={"+","-","*","/"}
        res=0
        for tok in tokens:
            if tok not in signs:
                stack.append(int(tok))
            else:
                if tok=="+":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(a + b)
                elif tok=="-":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(b - a)
                elif tok=="*":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(a * b))
                elif tok=="/":
                    a=stack.pop()
                    b=stack.pop()
                    stack.append(int(b / a))



        return stack.pop()




a=Solution()

tokens = ["2","1","+","3","*"]
print(a.evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(a.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(a.evalRPN(tokens))

