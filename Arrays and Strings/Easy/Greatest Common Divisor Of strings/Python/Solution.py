class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        
        def check(k):
            if n%k or m%k:
                return False
            n1, n2 = n//k, m//k
            base = str1[:k]
            return str1 == n1*base and str2 == n2*base

        for i in range(min(n,m), 0, -1):
            print(i)
            if check(i):
                return str1[:i]
        return ""