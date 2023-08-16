class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        j = 0
        for i in range(n):
            if j<m and t[i] == s[j]:
                j+=1
        if j==m:
            return True
        return False 