# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/21_generators/21_generators.md
# learned from: https://www.youtube.com/watch?v=bD05uGo_sVI
def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5,6])
for i in my_nums:
    print(i)