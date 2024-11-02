# Q1 
with open("practice.txt","w") as f:
    f.write("Hi everyone\nWe are learning pyhton I/O\nusing Java.\nI like programming in Java.")

with open("practice.txt","r+") as f:
    data=f.read()

new_data=data.replace("Java","python")
print(new_data)
 
with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt","r") as f:
    data2=f.read()
    
    if data2.find("learning"):
        print("learning found in the file")