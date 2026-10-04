class Solution:
    def checkValidString(self, s: str) -> bool:
        openstk=[]
        strstk=[]

        for i in range(len(s)):
            if s[i]=='(':
                openstk.append(i)
            
            elif s[i]=='*':
                strstk.append(i)

            else:
                if openstk:
                    openstk.pop()
                elif strstk:
                    strstk.pop()
                else:
                    return False
            
        while openstk and strstk:
            if openstk[-1]<strstk[-1]:
                openstk.pop()
                strstk.pop()
            else:
                return False
            
        return len(openstk)==0
            




