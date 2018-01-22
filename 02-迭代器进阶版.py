class MyList(object):
    def __init__(self, x):
        self.x = x

        self.current = 0  # 记录迭代次数

    def __iter__(self):
        """返回self，将自己变为迭代器"""
        return self

    def __next__(self):
        """获取下一个数"""
        if self.current < len(self.x):
            self.current += 1
            return self.x[self.current-1]
        else:
            raise StopIteration


mylist = MyList([11, 22, 33])
for i in mylist:
    print(i)
