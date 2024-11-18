#Enter marks of sunjects using user inputs and sore them as key:value pair
marks = {}
x = int(input("Enter marks in phy:"))
marks.update({"phy:" : x})

x = int(input("Enter marks in chem:"))
marks.update({"chem:" : x})

x = int(input("Enter marks in bio:"))
marks.update({"bio:" : x})
print(marks)
