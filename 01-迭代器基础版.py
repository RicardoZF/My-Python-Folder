class MyList(object):
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        myiterator = MyIterator(self.x)
        return myiterator


class MyIterator(object):
    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current < len(self.mylist):
            self.current += 1
            return self.mylist[self.current-1]
        else:
            raise StopIteration


mylist = MyList([11,22,33])

for i in mylist:
    print(i)