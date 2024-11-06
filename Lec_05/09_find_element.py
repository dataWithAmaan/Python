# print element and find element in the list 

# nums = [1,4,9,16,25,36,49,64,81,100]
# for i in nums:
#     print(i)

nums = (1,4,9,16,25,36,49,64,81,100)
x = 25
for el in nums:
    if el == x:
        print("Found", x, "at position", nums.index(x))