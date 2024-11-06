# palindrome
list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abf", 1]

if list1 == list1[::-1]:
    print("List 1 is a palindrome")
if list2 == list2[::-1]:
    print("List 2 is a palindrome")
if list1 != list1[::-1] and list2 != list2[::-1]:
    print("Neither list is a palindrome")
