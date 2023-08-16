class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        start = 0
        end = 0
        max_vc = 0
        vowels = ["a", "e", "i", "o", "u"]
        vc = 0
        for i in range(n):
            if s[end] in vowels:
                vc+=1
            if end-start+1 == k:
                max_vc = max(max_vc, vc)
                if s[start] in vowels:
                    vc-=1
                start+=1
            end+=1
        return max_vc