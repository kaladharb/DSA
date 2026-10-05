class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]

        for ch in s:
            if ch == '(':
                stk.append(0)
            else:
                inside = stk.pop()

                if inside == 0:
                    score = 1
                else:
                    score = 2 * inside

                stk[-1] += score

        return stk[0]


                