class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        n = len(word_list)
        start, end = 0, n-1
        while start<end:
            word_list[start], word_list[end] = word_list[end], word_list[start]
            start+=1
            end-=1
        return " ".join(i for i in word_list if i!='').strip()
