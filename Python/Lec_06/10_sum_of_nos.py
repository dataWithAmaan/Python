# Recursive function to find the sum of n natural nos 

def sum_natural(n):
    if n == 0:
        return 
    else:
        return n + sum_natural(n-1)

print(sum_natural(3))