class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        i, j= 0, 0
        turn = 1
        while i < len(word1) and j < len(word2):
            if turn == 1:
                merged_str+=word1[i]
                turn = 2
                i+=1
            else:
                merged_str+=word2[j]
                turn = 1
                j+=1
        if i<len(word1):
            merged_str+=word1[i:]
        if j<len(word2):
            merged_str+=word2[j:]
        return merged_str