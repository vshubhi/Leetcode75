class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.timex = []
        self.start = 0
        self.end = 0

    def ping(self, t: int) -> int:
      self.counter+=1
      self.timex.append(t)

      self.end = len(self.timex)-1
      startTime = t-3000
      endTime = t
      # print(self.timex, startTime, self.start, self.end)
      while self.start<=self.end and self.timex[self.start] < startTime:
          self.start+=1
          self.counter-=1

      return self.counter

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)