class Solution:
    def reverseVowels(self, s: str) -> str:
        n =  len(s)
        start = 0
        end = n-1
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        while(start<end):
            while start<end and s[start].lower() not in vowels:
                start+=1
            while start<end and s[end].lower() not in vowels:
                end -=1
                
            temp = s[start]
            s = s[:start] + s[end] + s[start+1:]
            s = s[:end] + temp + s[end+1:]
            start+=1
            end-=1
        return s