import os.path
from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read().split("\n")
        for product in products:
            print(product)
        file.close()

    def add(self, *args):
        file = open(self.__file_name, "a+")
        file_stream = file.tell()
        file.seek(0)
        products = file.read().splitlines()
        if len(products) == 0:
            for arg in args:
                file.write(f"{arg.__str__()}\n")
        else:
            for arg in args:
                if arg.__str__() in products:
                    print(f"Продукт {arg.__str__()} уже есть в магазине")
                else:
                    file.seek(file_stream)
                    file.write(f"{arg.__str__()}\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
