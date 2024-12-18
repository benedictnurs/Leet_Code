class RecentCounter:
    def __init__(self):
        self.ping_list = []

    def ping(self, t: int) -> int:
        self.ping_list.append(t)
        while self.ping_list[0] < t - 3000:
            self.ping_list.pop(0)
        return len(self.ping_list)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)