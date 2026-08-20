class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        sk=[]

        for i in tokens:
            if i not in "+-*/":
                sk.append(int(i))
            else:
                b=sk.pop()
                a=sk.pop()

                if i=="+":
                    sk.append(a+b)
                elif i=="-":
                    sk.append(a-b)
                elif i=="*":
                    sk.append(a*b)
                else:
                    sk.append(int(a/b))
        return sk[-1]