class MinStack(object):

    def __init__(self):
        self.stack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.insert(0, val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop(0)

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[0]
        else:
            return None

        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return min(self.stack)
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()