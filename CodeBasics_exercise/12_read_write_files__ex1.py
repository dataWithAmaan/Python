# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/read_write_file_exercise.md
word_stats={}

with open("D:\Amaan notes\Data Science\Python\CodeBasics_exercise\poem.txt","r") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word not in word_stats:
                word_stats[word] = 1
            else:
                word_stats[word] += 1
print(word_stats)

word_occurence = list(word_stats.values())
max_count = max(word_occurence)
print("max no of times word occured is: ",max_count)

print("The word that occured maximum no of times is: ")
for word, count in word_stats.items():
    if count == max_count:
        print(word)
