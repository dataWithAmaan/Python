# public and private attributes 
class bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #private attribute

r = bank("Amaan",0)
print(r.name,r.balance)