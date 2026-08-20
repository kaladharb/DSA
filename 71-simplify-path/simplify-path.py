class Solution:
    def simplifyPath(self, path: str) -> str:
        direct=path.split('/')
        stk=[]

        for i in direct:
            if i=="..":
                if len(stk)!=0:
                    stk.pop()
            
            elif i not in ['.','']:
                stk.append(i)
        return '/'+'/'.join(stk)



        


        