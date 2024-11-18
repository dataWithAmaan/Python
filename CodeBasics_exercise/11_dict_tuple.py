# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_tuple_exercise.md
import statistics
# Q1=>
population = {
    "china": 	143,
    "india": 	136,
    "usa": 32,
    "paskistan": 21,
}

# 1.)
x = input()
# a)
if x=="print":
    for country in population:
        print(f"{country}==> {population[country]}")
# b)
if x=="add":
    country = input("Enter country: ")
    if country in population:
        print("This country already exist!")
    else:
        value = int(input("Enter population: "))
        population[country] = value
        print(population)\
# c)
if x=="remove":
    country = input("Enter country: ")
    if country in population:
        del population[country]
    else:
        print("This country does not exist!")
    for country in population:
        print(f"{country}==> {population[country]}")
# d)
query = input("Enter country name for query: ")
if query in population:
    print(population[query])
else:
    print("This country does not exist!")

# 2.)
stock = {
    "info": [600,630,616.67],
    "ril": [1430,1490,1567],
    "mtl": [234,180,160]
}
# a)
x = input()
if x=="print":
    for company in stock:
        avg = stock[company]
        print(f"{company}==> {stock[company]}==> {statistics.mean(avg)}")
# b)
elif x == "add":
    company = input("Enter company name: ")
    price = input("Enter stock price: ")

    if company in stock:
        stock[company].append(price)
        print(f"Added {price} to {company}")
        print(stock)
    else:
        stock[company] = [price]
        print(f"Created new entry for {company} with price {price}")
        print(stock)

# 3.)
def circle_calc():
    radius = float(input("Enter radius: "))
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14* radius
    diameter = 2 * radius
    print(f"radius = {radius}, area = {area}, circumference = {circumference}, diameter = {diameter}")
circle_calc()
