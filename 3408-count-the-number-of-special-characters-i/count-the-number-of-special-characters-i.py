class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        n=len(word)
        ss=''
        for i in range(n):
            s=word[i].upper()
            if word[i].islower():
                if s in word and s not in ss:
                    c+=1
                    ss+=s
        return c
        