# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/read_write_file_exercise.md
with open("D:\Amaan notes\Data Science\Python\CodeBasics_exercise\stocks.csv",'r') as f, open("D:\Amaan notes\Data Science\Python\CodeBasics_exercise\output.csv",'w') as out:
    out.write("company Name, PE Ratio, PB Ratio\n")
    next(f)
    for lines in f:
        line = lines.split(",")
        stock = line[0]
        price = float(line[1])
        eps = float(line[2])
        bv = float(line[3])
        pe  = round(price/eps)
        pb = round(price/bv)
        out.write(f"{stock},{pe},{pb}\n")