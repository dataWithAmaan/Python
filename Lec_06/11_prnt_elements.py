# recursive function to print all elements in the list 

def print_elements(my_list,idx=0):
    if idx==len(my_list):
        return
    else:
        print(my_list[idx])
        print_elements(my_list,idx+1)

fruits = ["mango","lichi","apple","banana"]
print_elements(fruits)