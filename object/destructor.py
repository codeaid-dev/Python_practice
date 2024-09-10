class Counter:
    count = 0
    def __init__(self):
        print('in',end=' ')
        Counter.count += 1
    def __del__(self):
        print('del',end=' ')
        Counter.count -= 1
    @classmethod
    def how_many(cls):
        return cls.count

a = Counter()
b = Counter()
Counter()
#Counter()
#a = None
c = Counter()
del b
print(Counter.how_many())