# check for word line by line  Q2

def check_for_word():
    word = "python"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                return line_no
            line_no += 1
    return "NOT FOUND"

result = check_for_word()
print(result)
