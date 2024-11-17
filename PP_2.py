class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Ціна не може бути від'ємною.")

    def display_info(self):
        print(f"Продукт: {self.name}, Ціна: {self.price} грн")

    @staticmethod
    def store_promotion():
        print("Сьогодні акція: Знижка 10% на всю техніку!")


class Laptop(Product):
    def __init__(self, name: str, price: float, brand: str, ram: int):
        super().__init__(name, price)
        self.brand = brand
        self.ram = ram

    def display_info(self):
        super().display_info()
        print(f"Бренд: {self.brand}, ОЗП: {self.ram} ГБ")

    def upgrade_ram(self, additional_ram: int):
        self.ram += additional_ram
        print(f"ОЗП оновлено. Нова ОЗП: {self.ram} ГБ")


class Smartphone(Product):
    def __init__(self, name: str, price: float, brand: str, battery_capacity: int):
        super().__init__(name, price)
        self.brand = brand
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Бренд: {self.brand}, Ємність батареї: {self.battery_capacity} мА·г")

    def charge(self):
        print(f"{self.name} заряджається...")


class Warranty:
    def __init__(self, warranty_period: int):
        self.warranty_period = warranty_period

    def display_warranty(self):
        print(f"Гарантійний термін: {self.warranty_period} місяців")


class LaptopWithWarranty(Laptop, Warranty):
    def __init__(self, name: str, price: float, brand: str, ram: int, warranty_period: int):
        Laptop.__init__(self, name, price, brand, ram)
        Warranty.__init__(self, warranty_period)

    def display_info(self):
        super().display_info()
        self.display_warranty()


if __name__ == "__main__":
    product1 = Product("Миша", 500)
    laptop1 = Laptop("Ноутбук Acer", 20000, "Acer", 16)
    smartphone1 = Smartphone("iPhone", 30000, "Apple", 4000)
    laptop_with_warranty = LaptopWithWarranty("MacBook", 50000, "Apple", 32, 24)

    product1.display_info()
    laptop1.display_info()
    laptop1.upgrade_ram(8)

    smartphone1.display_info()
    smartphone1.charge()

    laptop_with_warranty.display_info()

    Product.store_promotion()

    product1.price = 450
    product1.display_info()