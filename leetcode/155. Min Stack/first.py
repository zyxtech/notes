class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataList = []

    def push(self, x: int) -> None:
        self.dataList.append(x)

    def pop(self) -> None:
        return self.dataList.pop()

    def top(self) -> int:
        return self.dataList[-1]

    def getMin(self) -> int:
        return min(self.dataList)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    obj = MinStack()
    obj.push("x")
    param_4 = obj.getMin()
    print(param_4)
