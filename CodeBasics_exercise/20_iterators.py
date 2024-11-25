# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/20_Iterators/20_Iterators.md
class Fibonacci():
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < self.limit:
            fib = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return fib
        else:
            raise StopIteration

fibonacci = Fibonacci(10)
for num in fibonacci:
    print(num)