class RandomizedSet:

    def __init__(self):
        self.randset = set()

    def insert(self, val: int) -> bool:
        if val not in self.randset:
            self.randset.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randset:
            self.randset.remove(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        if self.randset:
            return random.choice(list(self.randset))
        else:
            return None


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()