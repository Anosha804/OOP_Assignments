# 18. Property Decorators: @property, @setter, and @deleter
# Assignment: Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to 
# update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        del self._price

p = Product(100)
p.price = 200  # Update price
del p.price    # Delete price