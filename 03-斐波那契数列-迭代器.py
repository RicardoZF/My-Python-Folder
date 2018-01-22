class My_Iter(object):
    count = 0

    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if My_Iter.count < self.num:
            a = self.a
            self.a, self.b = self.b, self.a + self.b
            My_Iter.count += 1
            return a
        else:
            self.count = 0
            raise StopIteration


myiter = My_Iter(3)
for i in myiter:
    print(i)