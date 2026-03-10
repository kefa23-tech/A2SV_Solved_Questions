class RecentCounter:

    def __init__(self):
        self.recents = []
        self.pings = 0      

    def ping(self, t: int) -> int:
       
        self.recents.append(t)
        self.pings+=1
        while self.recents[0] < t - 3000:
            self.recents.pop(0)
        return len(self.recents)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)