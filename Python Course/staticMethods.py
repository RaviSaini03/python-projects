class calci:

    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b
    
c = calci(6)
print(c.num)
c.addToNum(12)
print(c.num)
print(calci.add(6, 3))
print(c.add(4, 6))