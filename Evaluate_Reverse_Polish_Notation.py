class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        if len(tokens)==1:
            temp=tokens[0]
        else:
            for i in range(len(tokens)):
                if tokens[i] in "+-/*":
                    op_2=stack.pop()
                    op_1=stack.pop()
                    temp=str(int(eval(op_1+tokens[i]+op_2)))
                    stack.append(temp)
                else:
                    stack.append(tokens[i])
        return int(temp)
