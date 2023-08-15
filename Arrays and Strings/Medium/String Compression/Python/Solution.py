class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        n = len(chars)
        while i<n:
            gpl = 1
            while(i+gpl<n and chars[i+gpl]==chars[i]):
                gpl+=1
            chars[res] = chars[i]
            res+=1
            if gpl>1:
                str_gpl = str(gpl)
                chars[res:res+len(str_gpl)] = list(str_gpl)
                res+=len(str_gpl)
            i+=gpl
        return res
      


