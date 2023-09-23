class Solution:
    def removeStars(self, s: str) -> str:
        stk = [] 
        for ch in s:
            if ch == "*" and stk:
                del stk[len(stk)-1]
                # print(stk)
            else:
                stk.append(ch)
        return "".join(x for x in stk)

        