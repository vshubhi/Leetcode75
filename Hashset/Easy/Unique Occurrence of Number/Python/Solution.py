class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for num in arr:
            if num not in hm:
                hm[num] = 0
            hm[num]+=1
        if len(set(hm.values())) != len(set(arr)):
            return False
        return True
