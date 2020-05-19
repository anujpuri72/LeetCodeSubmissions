class StockSpanner:

    def __init__(self):
        self.l = []

    def next(self, price: int) -> int:
        count = 1
        while(len(self.l) > 0 and self.l[-1][0] <= price):
            a, b = self.l.pop()
            count += b
        self.l.append([price, count])
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
