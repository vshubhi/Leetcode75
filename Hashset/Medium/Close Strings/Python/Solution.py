class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        sw1 = set(word1)
        sw2 = set(word2)
        hm1 = {}
        hm2 = {}
        for ch in word1:
            if ch not in hm1:
                hm1[ch] = 0
            hm1[ch] += 1
        for ch in word2:
            if ch not in hm2:
                hm2[ch] = 0
            hm2[ch] += 1
        x = sorted(list(hm1.values()))
        y = sorted(list(hm2.values()))
        # print(sw1, sw2, x, y)
        if sw1 == sw2 and x == y:
            return True
        return False