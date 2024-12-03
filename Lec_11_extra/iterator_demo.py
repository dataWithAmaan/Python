# https://www.youtube.com/watch?v=Dyu08G2l71c

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

value = TopTen()
for i in value:
    print(i)

'''
lst = [1,2,3,4,5,6]
x = iter(lst) # iter creates an object 
print(x.__next__())
print(x.__next__())
print(next(x))
'''