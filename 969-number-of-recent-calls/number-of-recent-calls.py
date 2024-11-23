class RecentCounter:

    def __init__(self):
        self.ping_list = []

    def ping(self, t: int) -> int:
        count = 0
        ex_range = [t - 3000, t]
        self.ping_list.append(t)
        while self.ping_list[0] < ex_range[0]:
            self.ping_list.pop(0)
        return len(self.ping_list)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)