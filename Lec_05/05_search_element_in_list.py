# search element in the list
l = (1,4,9,16,25,36,49,64,81,100)
print(l)
a = int(input("Enter number to be searched:"))

i = 0
while i<len(l):
    if(l[i] == a):
        print("Element found at index",i)
    i += 1