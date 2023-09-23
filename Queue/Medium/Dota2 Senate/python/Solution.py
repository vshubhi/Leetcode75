class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dire = deque()
        for i in range(len(senate)):
            if senate[i]=="R":
                rad.append(i)
            else:
                dire.append(i)
        n = len(senate)
        while rad and dire:
            if rad[0]<dire[0]:
                rad.append(n)
            elif rad and dire:
                dire.append(n)
            rad.popleft()
            dire.popleft()
            n+=1
        if rad:
            return "Radiant"
        return "Dire"