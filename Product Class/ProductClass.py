"""
Author: Tarun Balasubramaniam
Assignment Title: Product class
Assignment Description: Create a Product class and methods
Due Date: 8/28/2026
Date Created: 8/26/2026 
Date Last Modified: 8/27/2026
"""
class Product:
    def __init__ (self, code, price, count):
        self.code = code
        self.price = price
        self.count = count
    def set_code(self, code): # set the product code to parameter code
        self.code = code
    def get_code(self): # return the product code
        return self.code
    def set_price(self, price): # set the price to parameter price
        self.price = price
    def get_price(self): # return the price
        return self.price
    def set_count(self, count): # set the number of items in inventory to parameter count
        self.count = count
    def get_count(self): # return the count
        return self.count
    def add_inventory(self, amt): # increase inventory by parameter amt
        self.count += amt
    def sell_inventory(self, amt): # decrease inventory by parameter amt
        self.count -= amt

if __name__ == '__main__':
    #DATA ABSTRACTION
    a = Product("Apple", 0.40, 3)
    #OUTPUT
    print(f"Name: {a.get_code()} ")
    print(f"Price: {a.get_price():.2f}")
    print(f"Count: {a.get_count()}")

    #PROCESS
    #add 5 to inventory
    a.add_inventory(5)
    #OUTPUT
    print(f"Name: {a.get_code()} ")
    print(f"Price: {a.get_price():.2f}")
    print(f"Count: {a.get_count()}")

    #PROCESS
    a.set_code("Golden Delicious")
    a.set_price(0.55)
    a.sell_inventory(4)

    #OUTPUT
    print(f"Name: {a.get_code()} ")
    print(f"Price: {a.get_price():.2f}")
    print(f"Count: {a.get_count()}")

    #ASSUMPTIONS
    #expected arguments (str, float, int) are passed through the contructor
