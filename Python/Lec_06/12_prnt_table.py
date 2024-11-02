# print table using recursion 

def print_table(n,i,limit=11):
    if i==limit:
        return
    else:
        print(f"{n} * {i} = {n*i}")
        print_table(n,i+1,limit)
n = int(input("Enter a number: "))
print_table(n,1)


# Question made by me