class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value

    @price.deleter
    def price(self):
        del self.__price

p = Product(100)
print(p.price)

p.price = 200
print(p.price)

del p.price
#print(p.price)