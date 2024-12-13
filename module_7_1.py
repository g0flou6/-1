from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
         return f'{self.name}, {self.weight}, {self.category}.'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        products = open(Shop.__file_name)
        print(products.read())
        products.close()

    def add(self, *products):
        r_prod_file = open(Shop.__file_name, 'r')
        w_prod_file = open(Shop.__file_name, 'a')
        for product in products:
            if str(product) in r_prod_file.read():
                print(f'Продукт {product.name} уже есть в магазине.')
            else:
                w_prod_file.write(f'{product}\n')
        r_prod_file.close()
        w_prod_file.close()




sh = Shop()
p1 = Product('Carrot', 3.5, 'Vegetables')
p2 = Product('Apple', 0.5, 'Fruits')
p3 = Product('Carrot', 1.0, 'Vegetables')

sh.add(p3)
sh.add(p1)
sh.add(p2)

sh.get_products()